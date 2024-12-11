from django.shortcuts import render
from .models import SDVData
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def generate_sdv_graph(request):
    # Retrieve all SDV data
    data = SDVData.objects.all()
    timestamps = [entry.timestamp for entry in data]
    speeds = [entry.speed for entry in data]
    distances = [entry.distance_traveled for entry in data]
    
    # Generate a simple speed graph
    fig, ax = plt.subplots()
    ax.plot(timestamps, speeds, label="Speed (km/h)")
    ax.set_xlabel('Time')
    ax.set_ylabel('Speed (km/h)')
    ax.set_title('SDV Speed Over Time')
    ax.legend()

    # Convert plot to PNG image
    buf = io.BytesIO()
    FigureCanvas(fig).print_png(buf)
    img_str = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Render the template with the graph
    return render(request, 'sdv_data/graph.html', {'graph': img_str})
