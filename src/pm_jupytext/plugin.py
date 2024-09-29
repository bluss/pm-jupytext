
import jupytext
import nbformat

class PyHandler:
    """
    """

    @classmethod
    def read(cls, path):
        """
        Read a notebook, return json
        """
        path = path.removeprefix("jupytext:")
        with open(path, "r") as fp:
            nb = jupytext.read(fp)
            return nbformat.writes(nb)

    @classmethod
    def write(cls, file_content, path):
        """
        Write a notebook to an SFTP server.
        """
        raise NotImplementedError("Not a writable format")

    @classmethod
    def pretty_path(cls, path):
        return path

    @classmethod
    def listdir(cls, path):
        raise NotImplementedError
