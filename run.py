import nose
import sys
loop = 1
if sys.argv[1] == '--loop':
    loop = sys.argv[2]
inputs = ['', '--with-plan-loader', '--with-device-config', '--with-local-report','--verbosity=2']
for i in range(int(loop)):
    nose.run(argv=inputs)


