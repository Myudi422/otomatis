import requests

# Fungsi untuk mengirim permintaan scraping
def scrape_and_save(anime_ids):
    url = "https://ccgnimex.my.id/v2/android/scrapping/index.php"
    data = {"anime_id": anime_ids}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Data scraped dan disimpan untuk anime IDs:", anime_ids)
    else:
        print("Gagal menyimpan data untuk anime IDs:", anime_ids)

# URL untuk mendapatkan daftar anime IDs
api_url = "https://ccgnimex.my.id/v2/android/api_rilis.php"

while True:
    # Mendapatkan daftar anime IDs dari API
    response = requests.get(api_url)
    if response.status_code == 200:
        anime_ids_string = response.json().get('anime_ids', '')
        anime_ids = anime_ids_string.split(',')  # Memisahkan string menjadi daftar anime_ids
        print("Data anime IDs yang diperoleh:", anime_ids)
        if anime_ids:
            # Mengonversi daftar anime_ids menjadi string dengan setiap batch dipisahkan oleh koma
            for i in range(0, len(anime_ids), 5):
                batch_anime_ids = ','.join(anime_ids[i:i+5])
                scrape_and_save(batch_anime_ids)
        else:
            print("Tidak ada data anime IDs yang ditemukan.")
    else:
        print("Gagal mendapatkan daftar anime IDs dari API.")
