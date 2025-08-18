# QWEN 1.5-0.5b Super Fine Tuning

---

This project was created as an exercise in Super Fine Tuning Qwen 1.5 - 0.5b param model as it fit a few arbitrary criteria such as oss, small to load and well known.

---

## TODO

[x] Compare activation paths before and after sft for the same prompt for basic mech interp stuff.\

[o] Make the sft and model loading better (the code is the way it is to fit inside free tier of colab, once I get better at using colab, I think it can get better)\

[x] Increase epochs and steps\

[] Learn more about sft and how to make this sft better\

[-] Change benchmark to swe-bench or other similarly well known bench\ (won't do due to compute limitations)

[] Plot visuals for probability of next token.

[x] Plot delta logits for denoising prompts.

--- 
## Mech Interp stuff

Did some basic difference in logits plotting for denoising (clean -> corrupted prompt, png to be seen in the repo)

---
## Details about SFT

My main constraint was working on the free tier of colab and hence generating a whole bunch of tokens and training for larger amounts etc was not possible. Why did I not choose to get colab pro? Didn't feel like spending the monies on it.

How did I do it? QLoRA, deepmind/coding_contests dataset, loaded the model in 4bits cos quantization and model size, trained for 3 epochs, it's hard to truly see the results right now with the less tokens.
