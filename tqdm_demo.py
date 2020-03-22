import argh
from tqdm import tqdm, trange
import random
import time

# 100%|███████████████████████████████████████████████████| 10/10 [00:02<00:00,  4.99it/s] 
def tqdm_range():
    for i in tqdm(range(10)):
        time.sleep(0.2)

def tqdm_nested():
    for i in tqdm(range(10), desc='Outer loop'):
        for j in tqdm(range(random.randint(3,10)), desc='Inner Loop'):
            time.sleep(0.2)

def tqdm_non_uniform_progress(add_tot=False):
    max_iter = 100
    tot = 0

    if add_tot:
        bar = tqdm(desc='Updated progress bar', total=max_iter)
    else:
        bar = tqdm()

    while tot < max_iter:
        update_iter = random.randint(1, 5)
        bar.update(update_iter)
        tot += update_iter
        time.sleep(0.1)

def tqdm_updated_description():
    t = trange(100)
    for i in t:
        t.set_description(f'on iteration {i}')
        time.sleep(0.02)


if __name__ == '__main__':
    argh.dispatch_commands([tqdm_range, tqdm_nested, \
        tqdm_non_uniform_progress, tqdm_updated_description])