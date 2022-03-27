import custom
from custom import criterion
from custom.layers import *
from custom.config import config
from model import MusicTransformer
from data import Data
import utils
from midi_processor.processor import decode_midi, encode_midi

import datetime
import argparse

from tensorboardX import SummaryWriter


parser = custom.get_argument_parser()
args = parser.parse_args()
config.load(args.model_dir, args.configs, initialize=True)

# check cuda
if torch.cuda.is_available():
    config.device = torch.device('cuda')
else:
    config.device = torch.device('cpu')


current_time = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
gen_log_dir = 'logs/mt_decoder/generate_'+current_time+'/generate'
gen_summary_writer = SummaryWriter(gen_log_dir)

mt = MusicTransformer(
    embedding_dim=config.embedding_dim,
    vocab_size=config.vocab_size,
    num_layer=config.num_layers,
    max_seq=config.max_seq,
    dropout=0,
    debug=False)
mt.load_state_dict(torch.load(args.model_dir))
mt.test()

print(config.condition_file)
if config.condition_file is not None:
    inputs = np.array([encode_midi(config.condition_file)[:500]])

print("loading_inputs")
inputs = torch.from_numpy(inputs)
print("about to predict")
result = mt(inputs, config.length, gen_summary_writer)
print("generation finished:")

for i in result:
    print("test, sorry")
    print(i)

decode_midi(result, file_path=config.save_path)

gen_summary_writer.close()
