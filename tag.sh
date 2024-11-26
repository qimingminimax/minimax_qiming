#!/bin/bash
git add .
git commit -m "update"
git push
# 获取最新的 tag
latest_tag=$(git for-each-ref --sort=-taggerdate --format '%(refname:short)' refs/tags | sort -V  | tail -n 1)

# 提取版本号
version=$(echo "$latest_tag" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+$')

# 分解版本号为主版本号、次版本号和修订号
major=$(echo "$version" | cut -d. -f1)
minor=$(echo "$version" | cut -d. -f2)
patch=$(echo "$version" | cut -d. -f3)

# 计算下一个 tag 的版本号
next_patch=$((patch + 1))

# 构建新的 tag
new_tag="$major.$minor.$next_patch"

# echo
echo "新 tag: $new_tag"

# 打 tag
git tag "$new_tag"

# 推送 tag 到远端
git push origin "$new_tag"