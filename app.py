import gradio as gr
import joblib


joblib.dump(loaded_model, "population_model.joblib")
joblib.dump(saved_features, "population_features.joblib")


loaded_model = joblib.load("population_model.joblib")
saved_features = joblib.load("population_features.joblib")

def predict_population(
    Density_P_Km2,
    Land_Area_Km2,
    Fert_Rate,
    Median_Age,
    Urban_Pop_Percent,
    Migrants_Net,
    Yearly_Change_Percent
):
    new_country = pd.DataFrame([[
        Density_P_Km2,
        Land_Area_Km2,
        Fert_Rate,
        Median_Age,
        Urban_Pop_Percent,
        Migrants_Net,
        Yearly_Change_Percent
    ]], columns=saved_features)

    predicted_log_population = loaded_model.predict(new_country)[0]
    predicted_population = np.exp(predicted_log_population)

    return f"Predicted Population: {predicted_population:,.0f}"

import gradio as gr

def predict_population_ui(
    density, land_area, fertility, median_age,
    urban_pop, migrants, yearly_change
):
    result = predict_population(
        density, land_area, fertility, median_age,
        urban_pop, migrants, yearly_change
    )
    return result

custom_css = """
.gradio-container {
    max-width: 1100px !important;
    margin: auto !important;
}
#main-title {
    text-align: center;
    margin-bottom: 5px;
}
#subtitle {
    text-align: center;
    color: #64748b;
    margin-bottom: 25px;
}
.input-card, .output-card {
    border-radius: 14px !important;
    border: 1px solid #dbe4e8 !important;
    padding: 18px !important;
}
#predict-btn {
    background: #167d68 !important;
    color: white !important;
    border-radius: 10px !important;
}
#reset-btn {
    border-radius: 10px !important;
}
"""

with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="emerald",
        secondary_hue="slate",
        neutral_hue="slate"
    ),
    css=custom_css,
    title="World Population Predictor"
) as interface:

    gr.Markdown("# 🌍 World Population Predictor", elem_id="main-title")
    gr.Markdown(
        "Estimate a country's population using demographic and geographic data.",
        elem_id="subtitle"
    )

    with gr.Row():
        with gr.Column(scale=3):
            with gr.Group(elem_classes="input-card"):
                gr.Markdown("### 📊 Country Information")
                gr.Markdown("Enter the country's demographic details below.")

                with gr.Row():
                    density = gr.Number(
                        label="Population Density (people/km²)",
                        value=100,
                        minimum=0
                    )
                    land_area = gr.Number(
                        label="Land Area (km²)",
                        value=100000,
                        minimum=1
                    )

                with gr.Row():
                    fertility = gr.Number(
                        label="Fertility Rate",
                        value=2.0,
                        minimum=0
                    )
                    median_age = gr.Number(
                        label="Median Age",
                        value=30,
                        minimum=0,
                        maximum=100
                    )

                with gr.Row():
                    urban_pop = gr.Number(
                        label="Urban Population (%)",
                        value=50,
                        minimum=0,
                        maximum=100
                    )
                    migrants = gr.Number(
                        label="Net Migrants",
                        value=0
                    )

                yearly_change = gr.Number(
                    label="Yearly Population Change (%)",
                    value=1.0
                )

                with gr.Row():
                    predict_btn = gr.Button(
                        "🌍 Predict Population",
                        variant="primary",
                        elem_id="predict-btn"
                    )
                    reset_btn = gr.Button(
                        "↻ Reset Values",
                        elem_id="reset-btn"
                    )

        with gr.Column(scale=2):
            with gr.Group(elem_classes="output-card"):
                gr.Markdown("### 🎯 Prediction Result")
                result = gr.Textbox(
                    label="Estimated Population",
                    lines=3,
                    interactive=False,
                    placeholder="Your prediction will appear here."
                )

    input_components = [
        density, land_area, fertility, median_age,
        urban_pop, migrants, yearly_change
    ]

    predict_btn.click(
        fn=predict_population_ui,
        inputs=input_components,
        outputs=result
    )

    reset_btn.click(
        fn=lambda: [100, 100000, 2.0, 30, 50, 0, 1.0, ""],
        inputs=[],
        outputs=input_components + [result]
    )

interface.launch()