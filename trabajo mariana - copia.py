import os
from functools import partial
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

# Preguntas y opciones
questions = [
    {
        "question": "¿Cómo describirías tu estilo personal?",
        "options": [
            ("sofisticado y elegante", {"dior": 90, "chanel": 85, "tom ford": 80}),
            ("relajado y casual", {"hugo boss": 70, "lacoste": 65, "calvin klein": 60}),
            ("creativo y único", {"jean paul gaultier": 85, "custo": 80, "issey miyake": 75}),
            ("moderno y llamativo", {"versace": 90, "paco rabanne": 85, "dolce & gabbana": 80}),
        ],
    },
    {
        "question": "¿Qué tipo de fragancia prefieres?",
        "options": [
            ("fresca y floral", {"chanel": 85, "carolina herrera": 80, "marc jacobs": 75}),
            ("amaderada y especiada", {"tom ford": 90, "issey miyake": 80, "dior": 85}),
            ("cítrica y vibrante", {"hugo boss": 70, "lacoste": 65, "jean paul gaultier": 75}),
            ("dulce e intensa", {"paco rabanne": 90, "versace": 85, "dolce & gabbana": 80}),
        ],
    },
    {
        "question": "¿Qué accesorios usas con mayor frecuencia?",
        "options": [
            ("relojes o gafas de sol", {"hugo boss": 85, "lacoste": 80, "calvin klein": 75}),
            ("joyería elegante", {"dior": 90, "chanel": 85, "versace": 80}),
            ("sombreros o bufandas", {"jean paul gaultier": 85, "custo": 80, "marc jacobs": 75}),
            ("carteras llamativas", {"carolina herrera": 90, "dolce & gabbana": 85, "tom ford": 80}),
        ],
    },
    {
        "question": "¿Qué colores predominan en tu guardarropa?",
        "options": [
            ("negros, grises o blancos", {"calvin klein": 85, "hugo boss": 80, "tom ford": 75}),
            ("tonos pastel o claros", {"chanel": 90, "carolina herrera": 85, "marc jacobs": 80}),
            ("colores vivos y atrevidos", {"versace": 90, "paco rabanne": 85, "custo": 80}),
            ("estampados y combinaciones", {"jean paul gaultier": 85, "issey miyake": 80, "dolce & gabbana": 75}),
        ],
    },
    {
        "question": "¿Cuál sería tu destino ideal de vacaciones?",
        "options": [
            ("parís o milán", {"dior": 90, "chanel": 85, "carolina herrera": 80}),
            ("una playa relajante", {"lacoste": 85, "hugo boss": 80, "marc jacobs": 75}),
            ("una metrópolis moderna", {"tom ford": 90, "calvin klein": 85, "dolce & gabbana": 80}),
            ("un lugar exótico", {"versace": 90, "paco rabanne": 85, "issey miyake": 80}),
        ],
    },
    {
        "question": "¿Qué buscas en una prenda de vestir?",
        "options": [
            ("comodidad y simplicidad", {"calvin klein": 85, "lacoste": 80, "hugo boss": 75}),
            ("diseño innovador", {"jean paul gaultier": 90, "issey miyake": 85, "custo": 80}),
            ("elegancia clásica", {"chanel": 90, "dior": 85, "carolina herrera": 80}),
            ("atrevimiento y originalidad", {"versace": 90, "paco rabanne": 85, "dolce & gabbana": 80}),
        ],
    },
    {
        "question": "¿Qué actividad disfrutas más en tu tiempo libre?",
        "options": [
            ("cenar en un restaurante exclusivo", {"tom ford": 90, "dior": 85, "chanel": 80}),
            ("hacer deporte al aire libre", {"lacoste": 85, "hugo boss": 80, "calvin klein": 75}),
            ("visitar exposiciones de arte", {"marc jacobs": 90, "issey miyake": 85, "custo": 80}),
            ("salir a eventos sociales", {"versace": 90, "paco rabanne": 85, "dolce & gabbana": 80}),
        ],
    },
    {
        "question": "¿Qué tipo de calzado prefieres?",
        "options": [
            ("zapatos formales", {"hugo boss": 90, "calvin klein": 85, "tom ford": 80}),
            ("deportivos o casuales", {"lacoste": 85, "marc jacobs": 80, "custo": 75}),
            ("tacones o botas elegantes", {"chanel": 90, "dior": 85, "carolina herrera": 80}),
            ("sandalias o calzado llamativo", {"versace": 90, "dolce & gabbana": 85, "paco rabanne": 80}),
        ],
    },
    {
        "question": "¿Qué te define mejor en el trabajo?",
        "options": [
            ("profesionalismo y elegancia", {"dior": 90, "chanel": 85, "tom ford": 80}),
            ("eficiencia y practicidad", {"hugo boss": 85, "lacoste": 80, "calvin klein": 75}),
            ("creatividad y visión", {"jean paul gaultier": 90, "custo": 85, "marc jacobs": 80}),
            ("pasión y carisma", {"versace": 90, "dolce & gabbana": 85, "paco rabanne": 80}),
        ],
    },
    {
        "question": "¿Cuál es tu mayor prioridad en la vida?",
        "options": [
            ("éxito profesional", {"dior": 90, "tom ford": 85, "hugo boss": 80}),
            ("comodidad y estabilidad", {"calvin klein": 85, "lacoste": 80, "carolina herrera": 75}),
            ("expresar tu personalidad", {"jean paul gaultier": 90, "custo": 85, "marc jacobs": 80}),
            ("vivir momentos inolvidables", {"versace": 90, "dolce & gabbana": 85, "paco rabanne": 80}),
        ],
    },
]

# Clase principal
class QuestionnaireApp(App):
    def build(self):
        """Configura y lanza la aplicación."""
        self.title = "Encuesta de marcas"
        self.question_index = 0
        self.scores = {brand: 0 for brand in [
            "dior", "chanel", "tom_ford", "hugo_boss", "lacoste",
            "calvin_klein", "jean_paul_gaultier", "custo", "issey_miyake",
            "versace", "paco_rabanne", "dolce_gabbana"
        ]}
        self.layout = BoxLayout(orientation="vertical")
        self.show_question()
        return self.layout

    def show_question(self):
        """Muestra la pregunta actual y sus opciones."""
        self.layout.clear_widgets()
        if self.question_index < len(questions):
            question_data = questions[self.question_index]
            question_label = Label(
                text=question_data["question"], 
                size_hint_y=0.2, 
                font_size="18sp"
            )
            self.layout.add_widget(question_label)
            for option_text, option_scores in question_data["options"]:
                button = Button(
                    text=option_text, 
                    size_hint_y=None, 
                    height=50
                )
                # Usar `partial` para pasar argumentos al método
                button.bind(on_press=partial(self.record_answer, option_scores))
                self.layout.add_widget(button)
        else:
            self.show_results()

    def record_answer(self, scores, _):
        for brand, score in scores.items():
            # Reemplaza espacios por guiones bajos para las claves
            normalized_brand = brand.replace(" ", "_")
            if normalized_brand in self.scores:
                self.scores[normalized_brand] += score
        self.question_index += 1
        self.show_question()


    def show_results(self):
        """Muestra los resultados al usuario."""
        self.layout.clear_widgets()
        top_brand = max(self.scores, key=self.scores.get)
        result_label = Label(
            text=f"La marca que mejor te representa es: {top_brand.replace('_', ' ').title()}!",
            font_size="20sp"
        )
        self.layout.add_widget(result_label)

        # Mostrar imagen asociada
        image_path = f"{top_brand}.png"
        try:
            brand_image = Image(source=image_path, size_hint_y=0.7)
            self.layout.add_widget(brand_image)
        except Exception as e:
            fallback_label = Label(
                text=f"(No se encontró una imagen para {top_brand.replace('_', ' ').title()})",
                font_size="16sp"
            )
            self.layout.add_widget(fallback_label)

        # Botón para reiniciar
        restart_button = Button(text="Reiniciar", size_hint_y=None, height=50)
        restart_button.bind(on_press=lambda _: self.restart())
        self.layout.add_widget(restart_button)

    def restart(self):
        """Reinicia la encuesta."""
        self.question_index = 0
        self.scores = {brand: 0 for brand in self.scores}
        self.show_question()

# Ejecutar la app
if __name__ == "__main__":
    QuestionnaireApp().run()