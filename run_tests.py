import os
def run_behave_tests():
    os.system('behave --no-capture')

if __name__=="__main__":
    run_behave_tests()