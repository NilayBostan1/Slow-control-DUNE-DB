import logging

log_dict = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}
input_data = 'data'
list_data_date = ['April3', 'April4']
HV_file_names = [f'{input_data}/NP04_DCS_01_Heinz_V_{f}.csv' for f in list_data_date]
output_folder = 'data'


def configure_from_args(args):
    logging.basicConfig(level=log_dict[args.dateinfo])
    logging.info(f'Set log level to {args.dateinfo}')
    global output_folder; output_folder = args.outputfolder
    if args.datelist is not None:
        global HV_file_names
        HV_file_names = [f'{input_data}/NP04_DCS_01_Heinz_V_{f}.csv' for f in args.datelist]
