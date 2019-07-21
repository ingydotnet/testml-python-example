import re

from testml.bridge import TestMLBridge as Base

class TestMLBridge(Base):
    def something(self, string, replacement):
        return re.sub(r'%BOM%', replacement, string)
