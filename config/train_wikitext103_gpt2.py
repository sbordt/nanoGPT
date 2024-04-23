
out_dir = 'out-wikitext'

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'wikitext-gpt2'
wandb_run_name = 'mini-gpt'

dataset = 'wikitext-103'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256 # context of up to 256 previous characters

# these make the total batch size be ~0.5M
# 12 batch size * 1024 block size * 5 gradaccum * 8 GPUs = 491,520
batch_size = 12
block_size = 1024
#gradient_accumulation_steps = 5 * 8
gradient_accumulation_steps =  5  # smaller for wikitext-103

# these are smaller for the wikitext-103 dataset
max_iters = 1500
lr_decay_iters = 1500
warmup_iters = 200

# eval stuff
eval_interval = 1000
eval_iters = 200
log_interval = 10

# weight decay
weight_decay = 1e-1