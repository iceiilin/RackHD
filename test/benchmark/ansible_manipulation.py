from benchmark.utils.ansible_control import ansibleControl
from benchmark.utils.case_recorder import caseRecorder
from benchmark.utils import parser

ansible_ctl = ansibleControl()


def start():

    ansible_ctl.render_case_name('freestyle')
    ansible_ctl.setup_env()
    data_path = ansible_ctl.get_data_path_per_case()
    case_recorder = caseRecorder(data_path)
    case_recorder.write_interval(ansible_ctl.get_data_interval())
    case_recorder.write_start()
    ansible_ctl.start_daemon()

def stop():

    data_path = ansible_ctl.get_data_path_per_case()
    case_recorder = caseRecorder(data_path)
    ansible_ctl.collect_data()
    case_recorder.write_end()
    parser.parse(data_path)
