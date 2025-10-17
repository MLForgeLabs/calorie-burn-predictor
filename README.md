# Calorie Burn Predictor 🏃‍♂️

![Streamlit App](https://via.placeholder.com/800x400.png?text=Calorie+Burn+Predictor+App) <!-- Replace with your screenshot/GIF -->

Predict calories burned during exercise using an XGBoost model with a sleek Streamlit interface! Slide to set age, weight, duration, heart rate, and more to get accurate predictions (MAE ~1.06, R² ~0.99). Hosted on Hugging Face Spaces for free!

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/yourusername/calorie-burn-predictor) <!-- Update with your Space URL -->

Built by [@MLForgeLabs](https://x.com/MLForgeLabs) for #MLOps and #FitnessTech enthusiasts.

## Features
- **Interactive UI**: Adjust inputs with sliders for Gender, Age, Height, Weight, Duration, Heart Rate, and Body Temperature.
- **Accurate Model**: XGBoost trained on Kaggle data, tuned with GridSearchCV.
- **MLOps Ready**: Reproducible with `requirements.txt`, pickled model (JSON versioning planned), deployable via FastAPI.
- **Free Hosting**: Live on Hugging Face Spaces, deployable in minutes.

## Demo
Try it live: [Hugging Face Space](https://huggingface.co/spaces/yourusername/calorie-burn-predictor) <!-- Update with your Space URL -->

![Demo GIF](https://via.placeholder.com/600x300.png?text=Demo+GIF) <!-- Replace with your GIF -->

## Installation (Local)
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/calorie-burn-predictor.git
   cd calorie-burn-predictor```

2. Install Dependencies
    ```bash 
    pip install -r requirements.txt```

3. Run the app:
    ```bash
    streamlit run app.py```

    Open http://localhost:8501 in your browser.


## Deployment (Hugging Face Spaces)
1. Create a Space at [huggingface.co/new-space](https://huggingface.co/new-space).
2. Select **Streamlit** SDK, link this GitHub repo, and deploy.
3. Files needed:
   - `app.py`: Main Streamlit app.
   - `tuned_xgboost_model.pkl`: Trained XGBoost model.
   - `requirements.txt`: Dependencies (`streamlit`, `pandas`, `joblib`, `xgboost`).
4. Auto-builds on push. Check logs in "Settings" if errors occur.

## MLOps Notes
- **Reproducibility**: Pinned dependencies in `requirements.txt`.
- **Model Versioning**: Using pickled model; JSON format planned for XGBoost compatibility.
- **Next Steps**: Integrate MLflow for experiment tracking, DVC for data versioning, and FastAPI for API deployment.
- **Source**: Trained on [Kaggle dataset](https://www.kaggle.com/datasets/fmendes/exercise-and-calories-burned).

## Contributing
Fork, tweak, and PR! Ideas:
- Add feature importance plots.
- Save prediction history.
- Integrate MLflow/DVC.

## License
MIT License. See [LICENSE](LICENSE) for details.

## Connect
- X: [@MLForgeLabs](https://x.com/MLForgeLabs)
- GitHub: [yourusername](https://github.com/yourusername)
- Share your predictions and tag us! #MLOps #FitnessTech