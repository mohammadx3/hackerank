import re
import requests


class related_videos:
    def __init__(self,source):
        self.source = source
        self.pattern = r'watch\?v=.{1,11}'
        
    def get_vid_list(self) -> list:
        try:
            self.data = requests.get(self.source)
            if self.data.status_code != 200:
                raise Exception('No response from the link')
            self.source_id = self.source[32:44]
            self.element = re.findall(self.pattern,self.data.text)
            self.vidid_list = set(x.replace('watch?v=','') for x in self.element)
            if self.source_id in self.vidid_list:
                self.vidid_list.remove(self.source_id)
            return self.vidid_list
        except requests.exceptions.RequestException as E:
            print('Page cannnot be opened: ',E)
            return []
        except Exception as Ex:
            print('Url cannot be processed: ',Ex)
            return []
        
            
     