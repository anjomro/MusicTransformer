mkdir dataset
mkdir dataset/processed
mkdir model_dir


git clone https://github.com/jason9693/midi-neural-processor.git midi_processor
pip install -r requirements.txt
pip install pretty_midi progress tensorboardX

sh scrape.sh dataset
python preprocess.py dataset dataset/processed

python train.py -c config/base.yml config/config-train.yml -m model_dir
