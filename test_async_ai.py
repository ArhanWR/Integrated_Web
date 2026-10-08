import asyncio
import time

from api.proses_ai import model_random_forest, model_svm


async def test_async_models():
    print("=== PENGUJIAN ASYNC AI ===")
    print()

    input_text = "data pengujian"

    print(f"Input: {input_text}")
    print("Menjalankan Random Forest dan SVM...")
    print()

    start_time = time.time()

    result_rf, result_svm = await asyncio.gather(
        model_random_forest(input_text),
        model_svm(input_text)
    )

    end_time = time.time()

    duration = end_time - start_time

    print("Hasil Random Forest:")
    print(result_rf)
    print()

    print("Hasil Support Vector Machine:")
    print(result_svm)
    print()

    print(f"Total waktu eksekusi: {duration:.3f} detik")
    print()

    print("Perbandingan:")
    print("Jika sequential : 0.3 + 0.5 = 0.8 detik")
    print(f"Jika async      : sekitar 0.5 detik (hasil aktual: {duration:.3f} detik)")
    print()

    if duration < 0.7:
        print("SUCCESS!")
        print("Kedua model berjalan secara bersamaan menggunakan asyncio.gather().")
    else:
        print("WARNING!")
        print("Waktu eksekusi lebih lama dari yang diharapkan.")


if __name__ == "__main__":
    asyncio.run(test_async_models())