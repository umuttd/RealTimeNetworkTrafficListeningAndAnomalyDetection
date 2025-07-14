# Gerçek Zamanlı Ağ Trafiği Dinleme ve K-Means ile Anomali Tespiti

## 📖 Proje Tanımı  
Bu proje, gerçek zamanlı ağ trafiğini dinleyerek K-Means kümeleme algoritması ile anomali tespiti yapmayı amaçlar. TCP/IP paket başlıklarından çıkarılan özellikler kullanılarak normal ve anomalik trafik örnekleri ayrıştırılır. Özellikle SYN Flood, Port Tarama ve ICMP Flood (Ping Flood) saldırıları simüle edilerek model performansı ölçülmüştür :contentReference[oaicite:0]{index=0}.

## ✨ Özellikler
- **Gerçek zamanlı trafik dinleme:** Ağ arayüzünden gelen paketler anlık olarak işlenir.  
- **K-Means tabanlı kümeleme:** Anomali tespiti için basit ve hızlı bir yöntem.  
- **Doğruluk ve metrik raporu:** Doğruluk, yanlış pozitif/negatif oranı ve kesinlik hesaplanır.  
- **Saldırı simülasyonları:**  
  - SYN Flood (`hping3 -S <hedef_ip> -p 80 --flood`)  
  - Port Tarama (`masscan -p1-65535 <hedef_ip> --rate=1000`)  
  - ICMP Flood (`ping <hedef_ip> -s 65500 -f`) :contentReference[oaicite:1]{index=1}.

## 🛠️ Teknolojiler
- **Python 3.8+**  
- **scapy** – Gerçek zamanlı paket yakalama  
- **numpy, pandas** – Veri işleme  
- **scikit-learn** – K-Means algoritması  
- **hping3, masscan, ping** – Saldırı simülasyon araçları  
- **matplotlib (opsiyonel)** – Sonuçların görselleştirilmesi  

## 🚀 Kurulum & Çalıştırma

1. **Depoyu klonlayın**  
   ```bash
   git clone https://github.com/KULLANICI_ADINIZ/gercek-zamanli-anomali-tespiti.git
   cd gercek-zamanli-anomali-tespiti
