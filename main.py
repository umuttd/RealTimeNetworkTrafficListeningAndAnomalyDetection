import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import matplotlib.pyplot as plt
from scapy.layers.inet import TCP, IP
from scapy.all import sniff
from scapy.all import conf
print(conf.use_pcap)
import numpy as np

"""
# Performans metrikleri
metrics = ["Accuracy", "Precision", "False Positive Rate", "False Negative Rate"]
values = [0.88, 0.95, 0.1, 0.04]

# Grafik
plt.figure(figsize=(10, 6))
bars = plt.bar(metrics, values, color=['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#E91E63'])

# Her bir bar üzerinde değer gösterimi
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.05, f"{bar.get_height():.2f}",
             ha='center', va='bottom', color='white', fontsize=12, fontweight='bold')

# Grafik detayları
plt.title("Anomali Tespiti Başarı Oranları", fontsize=16)
plt.ylabel("Oran", fontsize=14)
plt.ylim(0, 1.1)  # Oranlar 0 ile 1 arasında olduğu için
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show() """


# 1. Veri İşleme ve Model Eğitimi
# Veri işleme ve model eğitimi
def process_and_train(data_path):
    data = pd.read_csv(data_path, header=None)
    selected_columns = [0, 4, 5]  # Sadece 3 özellik
    data_selected = data[selected_columns]

    scaler = MinMaxScaler()
    data_normalized = scaler.fit_transform(data_selected)

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data_normalized)

    print("Küme Merkezleri:", kmeans.cluster_centers_)
    return scaler, kmeans


def detect_anomaly(packet):
    if packet.haslayer(TCP):
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        packet_length = len(packet)
        proto = packet[IP].proto  # Protokol türü (ör. TCP=6)
        flags = packet[TCP].flags  # TCP bayrakları
        print(
            f"Gerçek Zamanlı Veri: [Kaynak Port: {src_port}, Hedef Port: {dst_port}, Paket Uzunluğu: {packet_length}, Protokol: {proto}]")

        # Veriyi normalize et ve anomali kontrolü yap
        try:
            packet_data = preprocess_packet(src_port, dst_port, packet_length)
            normalized_data = scaler.transform(packet_data)
            distance = np.min(kmeans.transform(normalized_data))

            if distance > threshold:
                print(f"⚠️ Anomali Tespit Edildi! Kaynak Port: {src_port}, Hedef Port: {dst_port}, Uzaklık: {distance}")
            else:
                print(f"✔️ Normal Trafik: Kaynak Port: {src_port}, Hedef Port: {dst_port}")
        except Exception as e:
            print(f"Veri işleme hatası: {e}")


def preprocess_packet(src_port, dst_port, packet_length):
    return [[src_port, dst_port, packet_length]]



if __name__ == "__main__":
    scaler, kmeans = process_and_train("KDDTrain+.txt")
    distances = np.min(kmeans.transform(scaler.transform(pd.read_csv("KDDTrain+.txt", header=None)[[0, 4, 5]])), axis=1)
    threshold = np.percentile(distances, 99)
    print(f"Eşik Değeri: {threshold}")

    sniff(filter="tcp", prn=detect_anomaly, count=50)
