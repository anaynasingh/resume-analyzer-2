from xhtml2pdf import pisa

def convert_html_to_pdf(html_string, output_path):
    """ Convert a given HTML string to a PDF file. """
    with open(output_path, 'wb') as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
    
    if pisa_status.err:
        print("An error occurred while creating the PDF.")
    else:
        print(f"PDF successfully created at {output_path}")
        
        
html_content = """
<html>
  <head>
    <style>
      body {
        font-family: Arial, sans-serif;
        font-size: 12px; /* Smaller text for fitting everything */
        margin: 0;
        padding: 0;
        line-height: 1.4;
        width: 100%;
        height: 100%;
        box-sizing: border-box;
      }
      h1 {
        font-size: 22px;
        text-align: center;
        margin-bottom: 5px;
      }
      h2 {
        font-size: 16px;
        color: #2c3e50;
        margin-top: 20px;
        margin-bottom: 5px;
      }
      h3 {
        font-size: 14px;
        color: #34495e;
        margin-bottom: 5px;
      }
      p, ul {
        margin: 0;
        padding: 0;
      }
      .section-title {
        font-weight: bold;
        color: #2c3e50;
      }
      .contact-info {
        text-align: center;
        margin-bottom: 15px;
        font-size: 14px;
      }
      .contact-info a {
        text-decoration: none;
        color: #0073e6;
      }
      .section {
        margin-bottom: 25px;
      }
      .experience-info, .education-info, .skills-list, .projects-list {
        margin-bottom: 15px;
      }
      .footer {
        text-align: center;
        font-style: italic;
        margin-top: 20px;
      }
      .content-wrapper {
        width: 100%;
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
      }
      .half-width {
        width: 48%;
        display: inline-block;
        vertical-align: top;
      }
      .full-width {
        width: 100%;
      }
      .inline-block {
        display: inline-block;
        width: 48%;
      }
    </style>
  </head>
  <body>
    <div class="content-wrapper">
      <!-- Header: Name and Contact Information -->
      <div class="contact-info">
        <h1>Aum Sathwara</h1>
        <p>Chicago, IL | 872-279-9667 | <a href="mailto:asathwara@hawk.iit.edu">asathwara@hawk.iit.edu</a> | 
        <a href="https://www.linkedin.com/in/yourprofile">LinkedIn</a> | <a href="https://yourportfolio.com">Portfolio</a></p>
      </div>

      <!-- Summary -->
      <div class="section">
        <h2 class="section-title">Summary</h2>
        <p>Computer Science graduate with expertise in machine learning and software engineering, focused on building and deploying scalable relevance models and algorithms. Proven track record in optimizing database performance and reducing latency, ensuring high availability for large user bases. Delivered AI models with 96% accuracy that significantly enhanced sales through targeted strategies. Passionate about leveraging data-driven insights to create innovative solutions and improve user experiences.</p>
      </div>

      <!-- Education -->
      <div class="section">
        <h2 class="section-title">Education</h2>
        <div class="half-width">
          <h3>Illinois Institute of Technology, Chicago, IL</h3>
          <p>Master of Applied Science, Computer Science, GPA 3.77/4 (May 2025)</p>
          <p>Key Courses: Data Mining, NLP, Machine Learning, Big Data, Software Development, Deep Learning</p>
        </div>
        <div class="half-width">
          <h3>Gujarat Technological University, India</h3>
          <p>Bachelor of Engineering, Computer Engineering, GPA 3.76/4 (May 2023)</p>
          <p>Key Courses: Cloud Computing, Computer Architecture, Computer Vision, Data Science, Operating Systems</p>
        </div>
      </div>

      <!-- Professional Experience -->
      <div class="section">
        <h2 class="section-title">Professional Experience</h2>
        <div class="experience-info">
          <h3>Software Developer Intern</h3>
          <p>Tatvasoft, Ahmedabad, India (Jun 2022 – Jul 2022)</p>
          <ul>
            <li>Developed a full-stack library management system using Java, Spring Boot, and MySQL, automating processes for 50,000 users.</li>
            <li>Optimized database performance by 20% through query execution plans, enhancing response time from 500ms to 400ms.</li>
            <li>Collaborated in an agile team to implement fault-tolerant authentication, reducing system errors by 60% and maintaining 99.9% uptime.</li>
          </ul>
        </div>
        <div class="experience-info">
          <h3>Data Scientist Intern</h3>
          <p>Adventure, Pune, India (Apr 2021 – Oct 2021)</p>
          <ul>
            <li>Built a language translation model using TensorFlow and PyTorch, achieving 96% accuracy and contributing to a 48% sales increase.</li>
            <li>Engineered a microservices architecture with Docker/Kubernetes, handling 20,000+ daily API requests and reducing latency by 25%.</li>
            <li>Optimized ad delivery pipelines with Kafka streams and Redis caching, improving ad relevance scores by 30%.</li>
          </ul>
        </div>
      </div>

      <!-- Projects -->
      <div class="section">
        <h2 class="section-title">Projects</h2>
        <div class="inline-block">
          <h3>Diabetic Retinopathy - <a href="https://github.com/yourproject">GitHub</a></h3>
          <ul>
            <li>Developed a hybrid Vision Transformer-CNN model, achieving 95% accuracy in early-stage retinopathy detection.</li>
            <li>Deployed on AWS SageMaker, reducing inference time to 2 seconds per image for real-time diagnostics.</li>
          </ul>
        </div>
        <div class="inline-block">
          <h3>Visual Question Answering Model - <a href="https://github.com/yourproject">GitHub</a></h3>
          <ul>
            <li>Created a hybrid Vision Transformer and BERT model for medical image analysis, achieving 94% accuracy on clinical datasets.</li>
            <li>Enhanced model robustness by 15% on noisy images through contrastive learning, deployed as a Flask web app for real-time support.</li>
          </ul>
        </div>
        <div class="inline-block">
          <h3>Riptidee</h3>
          <ul>
            <li>Developed a full-stack React/Node.js application with MongoDB to visualize real-time campaign metrics, supporting 1,000+ concurrent users.</li>
            <li>Reduced data retrieval latency by 25% through optimized MongoDB queries, enhancing performance across 10+ advertising channels.</li>
          </ul>
        </div>
      </div>

      <!-- Leadership Experience -->
      <div class="section">
        <h2 class="section-title">Leadership Experience</h2>
        <div class="experience-info">
          <h3>Technical Head</h3>
          <p>HackClub SVIT (Oct 2021 – May 2023)</p>
          <ul>
            <li>Led a student-run club focused on technical skill development through workshops and hackathons.</li>
            <li>Organized a 36-hour hackathon with 400+ participants, overseeing logistics and a team of 35 volunteers.</li>
            <li>Mentored 300 participants during a 24-hour ideation hackathon, providing technical guidance and feedback.</li>
          </ul>
        </div>
      </div>

      <!-- Technical Skills -->
      <div class="section">
        <h2 class="section-title">Technical Skills</h2>
        <ul class="skills-list">
          <li><strong>Programming Languages:</strong> Python, Java, JavaScript, SQL, R</li>
          <li><strong>Machine Learning:</strong> TensorFlow, PyTorch, Keras, Scikit-learn, OpenCV, Hugging Face</li>
          <li><strong>Data Engineering:</strong> Apache Spark, Kafka, ETL Pipelines, Pandas, NumPy, Flask</li>
          <li><strong>Cloud & DevOps:</strong> AWS (S3, Lambda), Docker, Kubernetes, CI/CD, Terraform, Azure</li>
          <li><strong>Tools:</strong> Git, Linux, Jenkins, Maven</li>
        </ul>
      </div>

      <div class="footer">
        <p>&copy; 2025 Aum Sathwara</p>
      </div>
    </div>
  </body>
</html>
"""



# Convert the HTML string to PDF
convert_html_to_pdf(html_content, 'output.pdf')