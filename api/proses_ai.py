import asyncio
import time

from fastapi import FastAPI, Query

app = FastAPI()


async def model_random_forest(input_text: str):
    """
    Simulasi model Random Forest.
    Delay 0.3 detik.
    """
    await asyncio.sleep(0.3)

    return {
        "model": "Random Forest",
        "prediction": "AMAN",
        "confidence": 0.92
    }


async def model_svm(input_text: str):
    """
    Simulasi model Support Vector Machine.
    Delay 0.5 detik.
    """
    await asyncio.sleep(0.5)

    return {
        "model": "Support Vector Machine",
        "prediction": "BAHAYA",
        "confidence": 0.87
    }


@app.get("/api/proses_ai")
async def proses_ai(input: str = Query(...)):
    """
    Endpoint untuk menjalankan dua model AI
    secara asynchronous menggunakan asyncio.gather().
    """

    start_time = time.time()

    try:
        # Menjalankan kedua model secara bersamaan
        result_rf, result_svm = await asyncio.gather(
            model_random_forest(input),
            model_svm(input)
        )

        end_time = time.time()
        duration = end_time - start_time

        return {
            "status": "success",
            "duration_seconds": duration,
            "results": {
                "model_rf": result_rf,
                "model_svm": result_svm
            }
        }

    except Exception:
        end_time = time.time()
        duration = end_time - start_time

        return {
            "status": "error",
            "duration_seconds": duration,
            "results": {
                "model_rf": None,
                "model_svm": None
            }
        }