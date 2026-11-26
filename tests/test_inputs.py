"""核验资料能完整读取，接续文件包含各自关联信息。"""
import unittest

from inspect_inputs import FILES, ROOT, inspect, lines, read


class InputTest(unittest.TestCase):
    def test_each_document_decodes(self):
        for name in FILES:
            with self.subTest(name=name):
                if name.endswith('.json'):
                    self.assertTrue(read(name))
                elif name.endswith('.ndjson'):
                    self.assertTrue(lines(name))
                else:
                    self.assertTrue((ROOT / name).read_text(encoding='utf-8').strip())

    def test_connected_materials(self):
        self.assertTrue(inspect())
