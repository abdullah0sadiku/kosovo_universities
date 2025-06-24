"""
Kosovo Universities Information System
A comprehensive GUI application for exploring universities, faculties, and departments in Kosovo.

Author: Kosovo University Explorer
Version: 2.0
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter import font as tkFont
import json
import os
from datetime import datetime

# Data structures
QYTETET = {
    1: "Gjilan",
    2: "Ferizaj", 
    3: "Prizren",
    4: "Prishtina",
    5: "Peja",
    6: "Gjakova",
    7: "Mitrovica",
    8: "Lipjan",
}

class University:
    """Represents a university with its location and faculties."""
    
    def __init__(self, name, city, faculties):
        self.name = name
        self.city = city
        self.faculties = faculties

    def __str__(self):
        return f"{self.name}, City: {self.city}, Faculties: {len(self.faculties)}"

    def to_dict(self):
        return {
            'name': self.name,
            'city': self.city,
            'faculties': [faculty.to_dict() for faculty in self.faculties]
        }

class Faculty:
    """Represents a faculty with its departments."""
    
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def __str__(self):
        return f"Faculty: {self.name}, Departments: {len(self.departments)}"

    def to_dict(self):
        return {
            'name': self.name,
            'departments': [dept.to_dict() for dept in self.departments]
        }

class Department:
    """Represents a department with its subjects."""
    
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def __str__(self):
        return f"Department: {self.name}, Subjects: {', '.join(self.subjects)}"

    def to_dict(self):
        return {
            'name': self.name,
            'subjects': self.subjects
        }

class UniversityDataManager:
    """Manages university data initialization and operations."""
    
    @staticmethod
    def initialize_data():
        """Initialize all university data."""
        
        # Computer Science and Engineering Departments
        dept_se = Department("Software Engineering", [
            "Advanced Programming", "Data Structures", "Algorithms", 
            "Web Development", "Software Engineering", "Database Systems"
        ])
        dept_cs = Department("Cybersecurity", [
            "Network Security", "Cryptography", "Ethical Hacking", 
            "Data Protection", "Digital Forensics"
        ])
        dept_it = Department("Information Technology", [
            "Operating Systems", "Computer Networks", "Database Management",
            "System Administration"
        ])
        dept_ai = Department("Artificial Intelligence", [
            "Machine Learning", "Computer Vision", "Natural Language Processing",
            "Neural Networks", "Deep Learning"
        ])
        dept_ce = Department("Computer Engineering", [
            "Computer Architecture", "Embedded Systems", "System Programming",
            "Hardware Design"
        ])
        
        # Engineering Departments
        dept_ee = Department("Electrical Engineering", [
            "Electronics", "Control Systems", "Signals and Systems",
            "Power Systems", "Telecommunications"
        ])
        dept_civil = Department("Civil Engineering", [
            "Structural Engineering", "Hydraulic Engineering", "Geotechnics",
            "Construction Management"
        ])
        dept_arch = Department("Architecture", [
            "Architectural Design", "Building Structures", "Urban Planning",
            "Interior Design"
        ])
        
        # Business and Economics Departments
        dept_finance = Department("Finance and Banking", [
            "Corporate Finance", "Investment Analysis", "Banking and Insurance",
            "Financial Markets"
        ])
        dept_management = Department("Management and Informatics", [
            "Strategic Management", "Management Information Systems", 
            "Digital Marketing", "Project Management"
        ])
        dept_accounting = Department("Accounting and Auditing", [
            "Financial Accounting", "Management Accounting", "Auditing",
            "Tax Planning"
        ])
        
        # Law and Political Science
        dept_law = Department("Law", [
            "Constitutional Law", "Criminal Law", "Civil Law",
            "International Law", "Commercial Law"
        ])
        dept_political = Department("Political Science", [
            "International Relations", "Comparative Politics", 
            "Public Administration", "Political Theory"
        ])
        
        # Medical Sciences
        dept_medicine = Department("General Medicine", [
            "Anatomy", "Physiology", "Pharmacology", "Pathology",
            "Internal Medicine", "Surgery"
        ])
        dept_dentistry = Department("Dentistry", [
            "Dental Prosthetics", "Oral Surgery", "Orthodontics",
            "Periodontics"
        ])
        dept_pharmacy = Department("Pharmacy", [
            "Pharmaceutical Chemistry", "Pharmacology", 
            "Pharmaceutical Technology", "Clinical Pharmacy"
        ])
        
        # Liberal Arts and Sciences
        dept_albanian_lit = Department("Albanian Language and Literature", [
            "Albanian Literature", "Albanian Linguistics", "Literary Theory"
        ])
        dept_english_lit = Department("English Language and Literature", [
            "English Literature", "Linguistics", "Translation Studies"
        ])
        dept_philosophy = Department("Philosophy", [
            "History of Philosophy", "Ethics", "Logic", "Metaphysics"
        ])
        dept_psychology = Department("Psychology", [
            "Developmental Psychology", "Cognitive Psychology", 
            "Clinical Psychology", "Social Psychology"
        ])
        dept_math = Department("Mathematics", [
            "Mathematical Analysis", "Algebra", "Statistics", "Applied Mathematics"
        ])
        dept_physics = Department("Physics", [
            "Classical Physics", "Quantum Physics", "Thermodynamics",
            "Electromagnetism"
        ])
        dept_chemistry = Department("Chemistry", [
            "Analytical Chemistry", "Biochemistry", "Organic Chemistry",
            "Inorganic Chemistry"
        ])
        dept_biology = Department("Biology", [
            "Genetics", "Ecology", "Molecular Biology", "Botany", "Zoology"
        ])
        
        # Education and Sports
        dept_primary_ed = Department("Primary Education", [
            "Pedagogy", "Didactics", "Child Psychology", "Curriculum Development"
        ])
        dept_preschool = Department("Preschool Education", [
            "Child Psychology", "Teaching Methodology", "Early Childhood Development"
        ])
        dept_physical_ed = Department("Physical Education", [
            "Exercise Physiology", "Sports Training", "Sports Psychology",
            "Kinesiology"
        ])
        
        # Agriculture and Veterinary
        dept_agribusiness = Department("Agribusiness", [
            "Agricultural Economics", "Agricultural Marketing", 
            "Farm Management", "Rural Development"
        ])
        dept_veterinary = Department("Veterinary Medicine", [
            "Veterinary Anatomy", "Veterinary Pathology", 
            "Animal Health", "Veterinary Surgery"
        ])
        
        # Arts and Design
        dept_graphic_design = Department("Graphic Design", [
            "Graphic Design", "Digital Illustration", "Typography",
            "Brand Design"
        ])
        dept_music = Department("Musicology", [
            "Music History", "Music Theory", "Composition", "Performance"
        ])
        
        # Create Faculties
        faculty_cse = Faculty("Faculty of Computer Science and Engineering", 
                             [dept_se, dept_cs, dept_it, dept_ai, dept_ce])
        faculty_eee = Faculty("Faculty of Electrical and Computer Engineering", 
                             [dept_ee, dept_ce])
        faculty_economics = Faculty("Faculty of Economics", 
                                   [dept_finance, dept_management, dept_accounting])
        faculty_law = Faculty("Faculty of Law", [dept_law, dept_political])
        faculty_medicine = Faculty("Faculty of Medicine", 
                                  [dept_medicine, dept_dentistry, dept_pharmacy])
        faculty_architecture = Faculty("Faculty of Architecture and Engineering", 
                                      [dept_arch, dept_civil])
        faculty_philology = Faculty("Faculty of Philology", 
                                   [dept_albanian_lit, dept_english_lit])
        faculty_philosophy = Faculty("Faculty of Philosophy", 
                                    [dept_philosophy, dept_psychology])
        faculty_natural_sciences = Faculty("Faculty of Mathematics and Natural Sciences", 
                                          [dept_math, dept_physics, dept_chemistry, dept_biology])
        faculty_education = Faculty("Faculty of Education", 
                                   [dept_primary_ed, dept_preschool])
        faculty_agriculture = Faculty("Faculty of Agriculture and Veterinary", 
                                     [dept_agribusiness, dept_veterinary])
        faculty_sports = Faculty("Faculty of Sport Sciences", [dept_physical_ed])
        faculty_arts = Faculty("Faculty of Arts", [dept_graphic_design, dept_music])
        
        # Create Universities
        universities = [
            University("University of Prishtina \"Hasan Prishtina\"", QYTETET[4], [
                faculty_cse, faculty_eee, faculty_economics, faculty_law, 
                faculty_medicine, faculty_architecture, faculty_philology, 
                faculty_philosophy, faculty_natural_sciences, faculty_education, 
                faculty_agriculture, faculty_sports, faculty_arts
            ]),
            University("Haxhi Zeka University", QYTETET[5], [
                faculty_economics, faculty_law, faculty_cse
            ]),
            University("University of Gjilan \"Kadri Zeka\"", QYTETET[1], [
                faculty_education, faculty_economics, faculty_cse
            ]),
            University("University of Prizren \"Ukshin Hoti\"", QYTETET[3], [
                faculty_education, faculty_economics, faculty_law, faculty_cse
            ]),
            University("University of Gjakova \"Fehmi Agani\"", QYTETET[6], [
                faculty_medicine, faculty_education, faculty_philology
            ]),
            University("University of Applied Sciences in Ferizaj", QYTETET[2], [
                faculty_cse, faculty_architecture, faculty_eee
            ]),
            University("University of Mitrovica \"Isa Boletini\"", QYTETET[7], [
                faculty_cse, faculty_economics, faculty_law
            ]),
        ]
        
        return universities

class UniversityGUI:
    """Main GUI application for Kosovo Universities Information System."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Kosovo Universities Information System v2.0")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f8f9fa')
        
        # Initialize data
        self.universities = UniversityDataManager.initialize_data()
        self.filtered_universities = []
        self.selected_university = None
        self.selected_faculty = None
        
        # Create custom fonts
        self.title_font = tkFont.Font(family="Arial", size=20, weight="bold")
        self.heading_font = tkFont.Font(family="Arial", size=14, weight="bold")
        self.normal_font = tkFont.Font(family="Arial", size=10)
        
        # Create GUI elements
        self.create_widgets()
        self.create_menu()
        
        # Load initial data
        self.load_initial_data()
        
    def create_menu(self):
        """Create application menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Export Data", command=self.export_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Statistics", command=self.show_statistics)
        view_menu.add_command(label="About", command=self.show_about)
        
    def create_widgets(self):
        """Create and arrange GUI widgets."""
        
        # Header frame
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(header_frame, text="Kosovo Universities Information System", 
                              font=self.title_font, bg='#2c3e50', fg='white')
        title_label.pack(expand=True)
        
        # Main container
        main_container = tk.Frame(self.root, bg='#f8f9fa')
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left panel (Controls)
        left_panel = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=1, width=350)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_panel.pack_propagate(False)
        
        # Right panel (Results)
        right_panel = tk.Frame(main_container, bg='white', relief=tk.RAISED, bd=1)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.create_left_panel(left_panel)
        self.create_right_panel(right_panel)
        
    def create_left_panel(self, parent):
        """Create the left control panel."""
        
        # Controls title
        controls_title = tk.Label(parent, text="Search & Filter", 
                                 font=self.heading_font, bg='white', fg='#2c3e50')
        controls_title.pack(pady=15)
        
        # Search frame
        search_frame = tk.LabelFrame(parent, text="Quick Search", font=self.normal_font,
                                    bg='white', fg='#34495e', padx=10, pady=10)
        search_frame.pack(fill=tk.X, padx=15, pady=10)
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.on_search_changed)
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, 
                               font=self.normal_font, width=30)
        search_entry.pack(fill=tk.X, pady=5)
        
        # City selection frame
        city_frame = tk.LabelFrame(parent, text="Select City", font=self.normal_font,
                                  bg='white', fg='#34495e', padx=10, pady=10)
        city_frame.pack(fill=tk.X, padx=15, pady=10)
        
        self.city_var = tk.StringVar()
        self.city_combo = ttk.Combobox(city_frame, textvariable=self.city_var, 
                                      values=["All Cities"] + list(QYTETET.values()), 
                                      state="readonly", font=self.normal_font, width=28)
        self.city_combo.pack(fill=tk.X, pady=5)
        self.city_combo.bind('<<ComboboxSelected>>', self.on_city_selected)
        self.city_combo.set("All Cities")
        
        # University selection frame
        uni_frame = tk.LabelFrame(parent, text="Select University", font=self.normal_font,
                                 bg='white', fg='#34495e', padx=10, pady=10)
        uni_frame.pack(fill=tk.X, padx=15, pady=10)
        
        self.uni_var = tk.StringVar()
        self.uni_combo = ttk.Combobox(uni_frame, textvariable=self.uni_var, 
                                     state="readonly", font=self.normal_font, width=28)
        self.uni_combo.pack(fill=tk.X, pady=5)
        self.uni_combo.bind('<<ComboboxSelected>>', self.on_university_selected)
        
        # Faculty selection frame
        faculty_frame = tk.LabelFrame(parent, text="Select Faculty", font=self.normal_font,
                                     bg='white', fg='#34495e', padx=10, pady=10)
        faculty_frame.pack(fill=tk.X, padx=15, pady=10)
        
        self.faculty_var = tk.StringVar()
        self.faculty_combo = ttk.Combobox(faculty_frame, textvariable=self.faculty_var, 
                                         state="readonly", font=self.normal_font, width=28)
        self.faculty_combo.pack(fill=tk.X, pady=5)
        self.faculty_combo.bind('<<ComboboxSelected>>', self.on_faculty_selected)
        
        # Buttons frame
        buttons_frame = tk.Frame(parent, bg='white')
        buttons_frame.pack(fill=tk.X, padx=15, pady=20)
        
        # Clear button
        clear_btn = tk.Button(buttons_frame, text="Clear All", command=self.clear_all,
                             bg='#e74c3c', fg='white', font=self.normal_font,
                             relief=tk.FLAT, padx=20, pady=8, cursor='hand2')
        clear_btn.pack(fill=tk.X, pady=5)
        
        # Statistics button
        stats_btn = tk.Button(buttons_frame, text="Show Statistics", 
                             command=self.show_statistics,
                             bg='#3498db', fg='white', font=self.normal_font,
                             relief=tk.FLAT, padx=20, pady=8, cursor='hand2')
        stats_btn.pack(fill=tk.X, pady=5)
        
    def create_right_panel(self, parent):
        """Create the right results panel."""
        
        # Results title
        results_title = tk.Label(parent, text="Information Display", 
                                font=self.heading_font, bg='white', fg='#2c3e50')
        results_title.pack(pady=15)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Main info tab
        self.info_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.info_frame, text="Main Information")
        
        # Details tab
        self.details_frame = tk.Frame(self.notebook, bg='white')
        self.notebook.add(self.details_frame, text="Detailed View")
        
        # Create text areas
        self.results_text = scrolledtext.ScrolledText(self.info_frame, wrap=tk.WORD, 
                                                     font=self.normal_font, height=25, width=60)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.details_text = scrolledtext.ScrolledText(self.details_frame, wrap=tk.WORD, 
                                                     font=self.normal_font, height=25, width=60)
        self.details_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
    def load_initial_data(self):
        """Load initial data and display welcome message."""
        self.update_university_list()
        self.display_welcome_message()
        
    def display_welcome_message(self):
        """Display welcome message in the results area."""
        welcome_text = """Welcome to Kosovo Universities Information System v2.0!

🎓 FEATURES:
• Explore universities across Kosovo
• Browse faculties and departments
• Search for specific programs
• View detailed statistics
• Export data functionality

🏛️ AVAILABLE CITIES:
"""
        for city in QYTETET.values():
            welcome_text += f"• {city}\n"
            
        welcome_text += f"""
📊 QUICK STATS:
• Total Universities: {len(self.universities)}
• Total Cities: {len(QYTETET)}
• Total Faculties: {sum(len(uni.faculties) for uni in self.universities)}

🔍 HOW TO USE:
1. Select a city or search for specific terms
2. Choose a university from the filtered list
3. Browse faculties and departments
4. Use the tabs to switch between views

Start exploring by selecting a city or using the search function!
"""
        
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, welcome_text)
        
    def on_search_changed(self, *args):
        """Handle search text changes."""
        search_term = self.search_var.get().lower()
        if len(search_term) >= 2:
            self.filter_universities_by_search(search_term)
        elif len(search_term) == 0:
            self.update_university_list()
            
    def filter_universities_by_search(self, search_term):
        """Filter universities based on search term."""
        filtered = []
        for uni in self.universities:
            # Search in university name
            if search_term in uni.name.lower():
                filtered.append(uni)
                continue
                
            # Search in faculty names
            for faculty in uni.faculties:
                if search_term in faculty.name.lower():
                    filtered.append(uni)
                    break
                    
                # Search in department names
                for dept in faculty.departments:
                    if search_term in dept.name.lower():
                        filtered.append(uni)
                        break
                if uni in filtered:
                    break
                    
        self.filtered_universities = filtered
        self.update_university_combo()
        self.display_search_results(search_term)
        
    def display_search_results(self, search_term):
        """Display search results."""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"Search Results for: '{search_term}'\n")
        self.results_text.insert(tk.END, "=" * 50 + "\n\n")
        
        if self.filtered_universities:
            for i, uni in enumerate(self.filtered_universities, 1):
                self.results_text.insert(tk.END, f"{i}. {uni.name}\n")
                self.results_text.insert(tk.END, f"   📍 Location: {uni.city}\n")
                self.results_text.insert(tk.END, f"   🏛️ Faculties: {len(uni.faculties)}\n\n")
        else:
            self.results_text.insert(tk.END, "No results found. Try different search terms.\n")
            
    def on_city_selected(self, event=None):
        """Handle city selection."""
        selected_city = self.city_var.get()
        
        if selected_city == "All Cities":
            self.filtered_universities = self.universities.copy()
        else:
            self.filtered_universities = [uni for uni in self.universities 
                                        if uni.city == selected_city]
        
        self.update_university_combo()
        self.display_city_results(selected_city)
        
    def display_city_results(self, city):
        """Display universities in selected city."""
        self.results_text.delete(1.0, tk.END)
        
        if city == "All Cities":
            self.results_text.insert(tk.END, "All Universities in Kosovo\n")
            self.results_text.insert(tk.END, "=" * 30 + "\n\n")
            
            for i, uni in enumerate(self.universities, 1):
                self.results_text.insert(tk.END, f"{i}. {uni.name}\n")
                self.results_text.insert(tk.END, f"   📍 {uni.city}\n")
                self.results_text.insert(tk.END, f"   🏛️ {len(uni.faculties)} faculties\n\n")
        else:
            self.results_text.insert(tk.END, f"Universities in {city}\n")
            self.results_text.insert(tk.END, "=" * 30 + "\n\n")
            
            if self.filtered_universities:
                for i, uni in enumerate(self.filtered_universities, 1):
                    self.results_text.insert(tk.END, f"{i}. {uni.name}\n")
                    self.results_text.insert(tk.END, f"   🏛️ {len(uni.faculties)} faculties\n\n")
            else:
                self.results_text.insert(tk.END, f"No universities found in {city}.\n")
                
    def update_university_list(self):
        """Update the list of universities to display."""
        self.filtered_universities = self.universities.copy()
        self.update_university_combo()
        
    def update_university_combo(self):
        """Update university combobox values."""
        uni_names = [uni.name for uni in self.filtered_universities]
        self.uni_combo['values'] = uni_names
        self.uni_combo.set('')
        
        # Clear faculty combo
        self.faculty_combo['values'] = []
        self.faculty_combo.set('')
        
    def on_university_selected(self, event=None):
        """Handle university selection."""
        selected_uni_name = self.uni_var.get()
        if not selected_uni_name:
            return
            
        # Find selected university
        self.selected_university = None
        for uni in self.filtered_universities:
            if uni.name == selected_uni_name:
                self.selected_university = uni
                break
                
        if not self.selected_university:
            return
            
        # Update faculty combobox
        faculty_names = [faculty.name for faculty in self.selected_university.faculties]
        self.faculty_combo['values'] = faculty_names
        self.faculty_combo.set('')
        
        # Display university info
        self.display_university_info()
        
    def display_university_info(self):
        """Display detailed university information."""
        if not self.selected_university:
            return
            
        uni = self.selected_university
        
        # Main info tab
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"{uni.name}\n")
        self.results_text.insert(tk.END, "=" * len(uni.name) + "\n\n")
        self.results_text.insert(tk.END, f"📍 Location: {uni.city}\n")
        self.results_text.insert(tk.END, f"🏛️ Number of Faculties: {len(uni.faculties)}\n\n")
        
        self.results_text.insert(tk.END, "FACULTIES:\n")
        self.results_text.insert(tk.END, "-" * 20 + "\n")
        
        for i, faculty in enumerate(uni.faculties, 1):
            self.results_text.insert(tk.END, f"{i}. {faculty.name}\n")
            self.results_text.insert(tk.END, f"   📚 {len(faculty.departments)} departments\n\n")
            
        # Details tab
        self.details_text.delete(1.0, tk.END)
        self.details_text.insert(tk.END, f"DETAILED VIEW: {uni.name}\n")
        self.details_text.insert(tk.END, "=" * 50 + "\n\n")
        
        for faculty in uni.faculties:
            self.details_text.insert(tk.END, f"🏛️ {faculty.name}\n")
            self.details_text.insert(tk.END, "-" * len(faculty.name) + "\n")
            
            for dept in faculty.departments:
                self.details_text.insert(tk.END, f"  📚 {dept.name}\n")
                self.details_text.insert(tk.END, f"     Subjects: {', '.join(dept.subjects[:3])}")
                if len(dept.subjects) > 3:
                    self.details_text.insert(tk.END, f" (+{len(dept.subjects)-3} more)")
                self.details_text.insert(tk.END, "\n\n")
            self.details_text.insert(tk.END, "\n")
            
    def on_faculty_selected(self, event=None):
        """Handle faculty selection."""
        selected_faculty_name = self.faculty_var.get()
        
        if not selected_faculty_name or not self.selected_university:
            return
            
        # Find selected faculty
        self.selected_faculty = None
        for faculty in self.selected_university.faculties:
            if faculty.name == selected_faculty_name:
                self.selected_faculty = faculty
                break
                
        if not self.selected_faculty:
            return
            
        # Display faculty details
        self.display_faculty_details()
        
    def display_faculty_details(self):
        """Display detailed faculty information."""
        if not self.selected_faculty:
            return
            
        faculty = self.selected_faculty
        
        # Main info tab
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"{faculty.name}\n")
        self.results_text.insert(tk.END, "=" * len(faculty.name) + "\n")
        self.results_text.insert(tk.END, f"🏛️ University: {self.selected_university.name}\n")
        self.results_text.insert(tk.END, f"📚 Number of Departments: {len(faculty.departments)}\n\n")
        
        self.results_text.insert(tk.END, "DEPARTMENTS & SUBJECTS:\n")
        self.results_text.insert(tk.END, "-" * 30 + "\n\n")
        
        for i, dept in enumerate(faculty.departments, 1):
            self.results_text.insert(tk.END, f"{i}. {dept.name}\n")
            self.results_text.insert(tk.END, "   📖 Subjects:\n")
            for subject in dept.subjects:
                self.results_text.insert(tk.END, f"   • {subject}\n")
            self.results_text.insert(tk.END, "\n")
            
    def clear_all(self):
        """Clear all selections and reset the interface."""
        self.city_var.set("All Cities")
        self.uni_var.set('')
        self.faculty_var.set('')
        self.search_var.set('')
        
        self.uni_combo['values'] = []
        self.faculty_combo['values'] = []
        
        self.selected_university = None
        self.selected_faculty = None
        self.filtered_universities = self.universities.copy()
        
        self.update_university_combo()
        self.display_welcome_message()
        
        # Clear details tab
        self.details_text.delete(1.0, tk.END)
        
    def show_statistics(self):
        """Display system statistics."""
        stats_window = tk.Toplevel(self.root)
        stats_window.title("System Statistics")
        stats_window.geometry("500x400")
        stats_window.configure(bg='white')
        
        # Title
        title_label = tk.Label(stats_window, text="Kosovo Universities Statistics", 
                              font=self.heading_font, bg='white', fg='#2c3e50')
        title_label.pack(pady=20)
        
        # Stats text
        stats_text = scrolledtext.ScrolledText(stats_window, wrap=tk.WORD, 
                                              font=self.normal_font, height=20, width=60)
        stats_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Calculate statistics
        total_unis = len(self.universities)
        total_faculties = sum(len(uni.faculties) for uni in self.universities)
        total_departments = sum(len(faculty.departments) 
                               for uni in self.universities 
                               for faculty in uni.faculties)
        total_subjects = sum(len(dept.subjects) 
                            for uni in self.universities 
                            for faculty in uni.faculties 
                            for dept in faculty.departments)
        
        # City statistics
        city_stats = {}
        for uni in self.universities:
            city = uni.city
            if city not in city_stats:
                city_stats[city] = {'unis': 0, 'faculties': 0}
            city_stats[city]['unis'] += 1
            city_stats[city]['faculties'] += len(uni.faculties)
        
        stats_content = f"""KOSOVO UNIVERSITIES SYSTEM STATISTICS
{'='*50}

📊 OVERALL STATISTICS:
• Total Universities: {total_unis}
• Total Faculties: {total_faculties}
• Total Departments: {total_departments}
• Total Subjects: {total_subjects}
• Cities with Universities: {len(city_stats)}

🏛️ UNIVERSITIES BY CITY:
{'-'*30}
"""
        
        for city, stats in city_stats.items():
            stats_content += f"📍 {city}:\n"
            stats_content += f"   • Universities: {stats['unis']}\n"
            stats_content += f"   • Faculties: {stats['faculties']}\n\n"
            
        stats_content += f"""
🎓 LARGEST UNIVERSITIES:
{'-'*25}
"""
        
        # Sort universities by number of faculties
        sorted_unis = sorted(self.universities, key=lambda x: len(x.faculties), reverse=True)
        for i, uni in enumerate(sorted_unis[:5], 1):
            stats_content += f"{i}. {uni.name}\n"
            stats_content += f"   📚 {len(uni.faculties)} faculties\n\n"
            
        stats_text.insert(tk.END, stats_content)
        stats_text.config(state=tk.DISABLED)
        
    def show_about(self):
        """Show about dialog."""
        about_text = """Kosovo Universities Information System v2.0

A comprehensive GUI application for exploring universities, 
faculties, and departments in Kosovo.

Features:
• University and faculty browsing
• Advanced search functionality
• Statistical analysis
• Data export capabilities
• User-friendly interface

Developed for educational purposes.
"""
        messagebox.showinfo("About", about_text)
        
    def export_data(self):
        """Export university data to JSON file."""
        try:
            data = {
                'export_date': datetime.now().isoformat(),
                'universities': [uni.to_dict() for uni in self.universities],
                'statistics': {
                    'total_universities': len(self.universities),
                    'total_faculties': sum(len(uni.faculties) for uni in self.universities),
                    'total_departments': sum(len(faculty.departments) 
                                           for uni in self.universities 
                                           for faculty in uni.faculties)
                }
            }
            
            filename = f"kosovo_universities_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
            messagebox.showinfo("Export Successful", 
                               f"Data exported successfully to {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export data: {str(e)}")

def main():
    """Main application entry point."""
    root = tk.Tk()
    app = UniversityGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()

