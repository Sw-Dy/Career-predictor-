from flask import Flask, render_template, request, jsonify
import predictor  # Importing the correct module

app = Flask(__name__)

# Serve trait.html at the root route
@app.route('/')
def trait():
    return render_template('index.html')

# Serve index.html at the /index route
@app.route('/trait')
def index():
    return render_template('trait.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            # Extract data from form
            data = [
                int(request.form['cognitive_score']),
                int(request.form['iq']),
                int(request.form['verbal_ability']),
                int(request.form['logical_reasoning']),
                int(request.form['memorizing_ability']),
                int(request.form['spatial_awareness']),
                request.form['remote'],
                request.form['motivation_level'],
                request.form['work_life_balance'],
                request.form['work_environment'],
                request.form['preferred_location'],
                request.form['travel_willingness'],
                request.form['career_growth'],
                request.form['work_hours_flexibility'],
                request.form['company_size_preference'],
                request.form['preferred_industry'],
                request.form['team_structure'],
                request.form['job_stability'],
                request.form['training_opportunities'],
                request.form['ethical_values'],
                request.form['preferred_work_style'],
                request.form['communication_style'],
            ]
            
            # Pass data to the prediction function in the predictor module
            career_path = predictor.predict_career(data)
            
            return render_template('index.html', prediction=career_path)
    
    except Exception as e:
        # Log the exception for debugging
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
