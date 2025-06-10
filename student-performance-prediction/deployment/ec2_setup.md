# 🚀 AWS EC2 Deployment Guide

This guide walks you through deploying the Flask API on an AWS EC2 instance.

---

## 🧱 Prerequisites
- AWS account
- PEM key pair (downloaded when launching EC2)

---

## 🖥️ Step 1: Launch EC2 Instance
1. Go to [EC2 Dashboard](https://console.aws.amazon.com/ec2)
2. Click "Launch Instance"
3. Select:
   - Ubuntu 22.04 LTS
   - t2.micro (Free Tier)
4. Add Storage (keep default)
5. Configure Security Group:
   - Allow **SSH (port 22)** from My IP
   - Allow **HTTP (port 80)** from Anywhere
   - Allow **Custom TCP (port 5000)** from Anywhere (for Flask dev server)
6. Launch and download the `.pem` file

---

## 🔐 Step 2: Connect via SSH
```bash
chmod 400 your-key.pem
ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>
```

---

## ⚙️ Step 3: Setup Python and Flask
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip git -y
pip3 install flask pandas scikit-learn xgboost joblib
```

---

## 📦 Step 4: Clone and Run Your App
```bash
git clone https://github.com/your-username/student-risk-predictor.git
cd student-risk-predictor/app
python3 app.py
```

Access your API from: `http://<EC2_PUBLIC_IP>:5000`
