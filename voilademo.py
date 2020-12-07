from notebook.notebookapp import list_running_servers
import time, glob

class pdfgrabber:

    def __init__(self):

        """Standard __init__ method.
        
        Attributes
        ----------

        files: list
            list of uploaded files
        current_file: str
            currently analyzed file
        
        file: upload widget
        select_file : selection widget
        out : output widget
        
        """

        self.files = None
        self.current_file = None

        # Create widgets
        self.file = ipw