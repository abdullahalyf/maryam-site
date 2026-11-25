# মরিয়মের ওয়েবসাইট — নিজের নামে চালু করা ও আপডেট করা

কোনো কোড জানা লাগবে না। শুধু ব্রাউজার আর GitHub অ্যাকাউন্ট লাগবে।

## ১. নিজের সাইট চালু করা (একবারই)
1. https://github.com এ অ্যাকাউন্ট খোলো (না থাকলে) এবং লগইন করো।
2. https://github.com/abdullahalyf/maryam-site খোলো। উপরে ডানে **Fork** চাপো → **Create fork**।
3. তোমার নতুন repo-তে গিয়ে **Settings** → বাঁ পাশে **Pages** চাপো।
4. **Build and deployment → Source** এর ড্রপডাউন থেকে **GitHub Actions** বেছে নাও।
5. উপরের মেনুতে **Actions** ট্যাবে যাও। সবুজ বাটন **"I understand my workflows, go ahead and enable them"** দেখলে সেটা চাপো।
6. বাঁ পাশে **Deploy to GitHub Pages** চাপো → ডানে **Run workflow** → **Run workflow**।
7. ১–২ মিনিট অপেক্ষা করো। সবুজ টিক এলে **Settings → Pages** এ গিয়ে লিংকটা দেখো। সাধারণত এমন হবে: `https://তোমার-ইউজারনেম.github.io/maryam-site/`
8. লিংকটা খোলো। না এলে `Ctrl + F5` চাপো।

## ২. আপডেট করা
GitHub-এ কোনো ফাইল বদলে **Commit changes** চাপলেই ১–২ মিনিটে সাইট নিজে আপডেট হয়।

**লেখা বদলাতে:** `personal/profile.yaml` খোলো → পেন্সিল (Edit) আইকন চাপো। নাম, CGPA, প্রজেক্ট, GitHub/LinkedIn লিংক সব এখানে। লাইনের শুরুর স্পেস যেমন আছে তেমন রাখবে। লিংকের ঘর ফাঁকা (`""`) থাকলে সেটা সাইটে দেখায় না।

**ছবি বদলাতে:** `personal/photos/` ফোল্ডারে যাও → **Add file → Upload files**। ছবির নাম **একই** রাখবে:
- `profile.jpg` বড় ছবি (এখন শুধু "MA" লেখা আছে), `avatar.jpg` ছোট চৌকো ছবি
- `project-1.jpg`, `project-2.jpg`… প্রজেক্টের ক্রম অনুযায়ী
- `edu-1.jpg` (ইউনিভার্সিটি), `edu-2.jpg` (কলেজ), `edu-3.jpg` (স্কুল) এডুকেশনের ছবি
- `hobby-1.jpg`, `hobby-2.jpg` শখের ছবি

**CV বদলাতে:** `personal/cv.pdf` নামে নতুন ফাইল আপলোড করো।

**নতুন ব্লগ:** `content/blog` → Add file → Create new file → নাম `my-post.md`। উপরে এটা লিখে নিচে লেখা দাও:
```
---
title: "শিরোনাম"
date: 2026-12-01
summary: "এক লাইনের সারাংশ"
cover: "my-post"
---
```
কভার ছবি `personal/blog/my-post.jpg` নামে আপলোড করো।

## কিছু ভেঙে গেলে
**Actions** ট্যাবে লাল দাগ দেখলে শেষ যে ফাইল বদলেছ সেটা আগের মতো করে দাও। সাধারণত `profile.yaml`-এ স্পেস বা উদ্ধৃতিচিহ্ন (") ভুল হলেই এমন হয়।
