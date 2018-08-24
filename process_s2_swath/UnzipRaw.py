import luigi
import os
from luigi import LocalTarget

class UnzipRaw(luigi.Task):
    pathRoots = luigi.DictParameter()

    def run(self):
        with self.output().open('w') as o:
            o.write('UnzipRaw')
    
    def output(self):
        outFile = os.path.join(self.pathRoots['state'], 'UnzipRaw.json')
        return LocalTarget(outFile)

