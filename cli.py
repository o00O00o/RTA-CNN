import re
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='RTA-CNN for AF Detection')
    parser.add_argument('--experiment-index', default=None, type=int, metavar='N', help='select the folder for validation')
    parser.add_argument('--arch', '-a', metavar='ARCH', default='RTA_CNN',choices=architectures.__all__, 
                        help='model architecture: ' + ' | '.join(architectures.__all__))
    parser.add_argument('--epochs', default=100, type=int, metavar='N', help='number of total epochs to run')
    parser.add_argument('--batchsize', default=48, type=int, metavar='N', help='mini-batch size (default: 16)')
    parser.add_argument('--lr', default=1e-4, type=float, metavar='LR', help='max learning rate')
    return parser


def parse_commandline_args():
    return create_parser().parse_args()


def parse_dict_args(**kwargs):
    def to_cmdline_kwarg(key, value):
        if len(key) == 1:
            key = "-{}".format(key)
        else:
            key = "--{}".format(re.sub(r"_", "-", key))
        value = str(value)
        return key, value

    kwargs_pairs = (to_cmdline_kwarg(key, value) for key, value in kwargs.items())
    cmdline_args = list(sum(kwargs_pairs, ()))


    return create_parser().parse_args(cmdline_args)


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def str2epochs(v):
    try:
        if len(v) == 0:
            epochs = []
        else:
            epochs = [int(string) for string in v.split(",")]
    except:
        raise argparse.ArgumentTypeError('Expected comma-separated list of integers, got "{}"'.format(v))
    if not all(0 < epoch1 < epoch2 for epoch1, epoch2 in zip(epochs[:-1], epochs[1:])):
        raise argparse.ArgumentTypeError('Expected the epochs to be listed in increasing order')
    return epochs