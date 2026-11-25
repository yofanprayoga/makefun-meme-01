// Entry for make.fun "Post the Meme, Win the Feed" (Node 22, stdlib only).
//
// The entry is the X post itself: POST.json at this repository's root names
// the post's address. This program copies POST.json to /output/POST.json,
// where the gate reads it, after refusing a placeholder or malformed URL
// so a bad address fails loudly instead of scoring zero silently.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

// An X post address: https://x.com/<handle>/status/<digits>
// (twitter.com, www./mobile. and /i/web/status/<id> spellings pass too).
const POST_URL = /^https:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\/[^/]+\/status\/\d+(\?.*)?$/;

const postPath = join(BOT_DIR, 'POST.json');
let post;
try {
  post = JSON.parse(readFileSync(postPath, 'utf8'));
} catch (err) {
  console.error(`POST.json could not be read from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}

if (typeof post?.url !== 'string' || !POST_URL.test(post.url)) {
  console.error('POST.json does not name a valid X post URL (https://x.com/<handle>/status/<id>).');
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(postPath, join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied to ${OUTPUT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
