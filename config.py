import logging

log_dict = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}
input_data = 'data'
list_data_date = ['April3', 'April4']
HV_file_names = [f'{input_data}/NP04_DCS_01_Heinz_V_{d}.csv' for d in list_data_date]
output_folder = 'data/output'


def configure_from_args(args):
    logging.basicConfig(level=log_dict[args.loglvl])
    logging.info(f'Set log level to {args.loglvl}')
    global output_folder; output_folder = args.outputfolder
    if args.datelist is not None:
        global HV_file_names
        HV_file_names = [f'{input_data_folder}/NP04_DCS_01_Heinz_V_{d}.csv' for d in args.datelist]
