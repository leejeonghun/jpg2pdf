import io
import sys
import mimetypes
import uuid
import json
import urllib.request


class MultiPartForm:
    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = uuid.uuid4().hex.encode('utf-8')

    def get_content_type(self):
        return f'multipart/form-data; boundary={self.boundary.decode("utf-8")}'

    def add_field(self, name, value):
        self.form_fields.append((name, value))

    def add_file(self, fieldname, filename, file_obj, mimetype=None):
        body = file_obj.read()
        if mimetype is None:
            mimetype = (
                mimetypes.guess_type(filename)[0] or
                'application/octet-stream'
            )
        self.files.append((fieldname, filename, mimetype, body))

    @staticmethod
    def _form_data(name):
        return ('Content-Disposition: form-data; '
                f'name="{name}"\r\n').encode('utf-8')

    @staticmethod
    def _attached_file(name, filename):
        return ('Content-Disposition: file; '
                f'name="{name}"; filename="{filename}"\r\n').encode('utf-8')

    @staticmethod
    def _content_type(ct):
        return 'Content-Type: {}\r\n'.format(ct).encode('utf-8')

    def __bytes__(self):
        buffer = io.BytesIO()
        boundary = b'--' + self.boundary + b'\r\n'

        for name, value in self.form_fields:
            buffer.write(boundary)
            buffer.write(self._form_data(name))
            buffer.write(b'\r\n')
            buffer.write(value.encode('utf-8'))
            buffer.write(b'\r\n')

        for f_name, filename, f_content_type, body in self.files:
            buffer.write(boundary)
            buffer.write(self._attached_file(f_name, filename))
            buffer.write(self._content_type(f_content_type))
            buffer.write(b'\r\n')
            buffer.write(body)
            buffer.write(b'\r\n')

        buffer.write(b'--' + self.boundary + b'--\r\n')
        return buffer.getvalue()


def validation(file):
    with open(file, 'rb') as f:
        form = MultiPartForm()
        form.add_file('file', file, file_obj=f)
        data = bytes(form)
        r = urllib.request.Request(
            'https://www.pdf-online.com/osa/validate.aspx', data=data)
        r.add_header('Content-type', form.get_content_type())
        r.add_header('Content-length', len(data))

        response = json.loads(urllib.request.urlopen(r).read().decode('utf-8'))
        return response['Result'] == 'Document validated successfully.'


if __name__ == '__main__':
    if validation(sys.argv[0]):
        print('valid')
    else:
        print('not vaild')
