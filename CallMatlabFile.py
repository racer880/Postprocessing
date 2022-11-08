import matlab.engine
eng = matlab.engine.start_matlab()
eng.cd(r'C:\Users\patrick.grubert\Downloads\Postprocessing', nargout=0)
eng.Test_Script()