# 🛡️ QUICK SETUP CARD - BRANCH PROTECTION
## Copy/Paste Reference for GitHub Settings

### STEP 1: Branch Protection Rule
**Branch name pattern:** `main`

### STEP 2: Check These Boxes (Critical!)
```
✅ Require a pull request before merging
  ├─ Required number of reviewers before merging: 2
  ├─ ✅ Dismiss stale pull request approvals when new commits are pushed
  ├─ ❌ Require review from code owners (Requires GitHub Pro - skip for now)
  └─ ✅ Restrict pushes that create files larger than 100MB

✅ Require status checks to pass before merging
  └─ ✅ Require branches to be up to date before merging

✅ Require conversation resolution before merging
✅ Require signed commits
✅ Require linear history
✅ Include administrators (SUPER IMPORTANT!)

❌ Allow force pushes (LEAVE UNCHECKED)
❌ Allow deletions (LEAVE UNCHECKED)
```

### STEP 3: After Saving Rule
Go to: Settings → Security & analysis

Enable:
```
✅ Dependency graph
✅ Dependabot alerts  
✅ Dependabot security updates
✅ Secret scanning
✅ Push protection
✅ Private vulnerability reporting
```

### 🎯 SUCCESS INDICATOR
After setup, you should see:
- "main branch is protected" green badge
- Cannot push directly to main
- Pull requests require 2 reviews

**Your IP is now FORTRESS-LEVEL protected!** 🏰💎⚡
