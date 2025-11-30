"""
Password Strength Checker - GUI Application
Modern, user-friendly interface built with tkinter
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from password_strength_checker import PasswordStrengthChecker
import json
from datetime import datetime


class PasswordStrengthGUI:
    """GUI application for password strength checking."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker - Cybersecurity Tool")
        self.root.geometry("900x750")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize checker
        self.checker = PasswordStrengthChecker()
        
        # Password variable
        self.password_var = tk.StringVar()
        self.password_var.trace('w', self.on_password_change)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface."""
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🔒 Password Strength Checker",
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Comprehensive Security Analysis Tool",
            font=('Arial', 10),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        subtitle_label.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Password input section
        input_frame = tk.LabelFrame(
            main_frame,
            text="Enter Password",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50',
            padx=15,
            pady=15
        )
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Password entry with show/hide toggle
        entry_frame = tk.Frame(input_frame, bg='#f0f0f0')
        entry_frame.pack(fill=tk.X)
        
        self.password_entry = tk.Entry(
            entry_frame,
            textvariable=self.password_var,
            font=('Arial', 14),
            show='*',
            width=40
        )
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.show_password_var = tk.BooleanVar()
        show_check = tk.Checkbutton(
            entry_frame,
            text="Show",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
            bg='#f0f0f0',
            font=('Arial', 10)
        )
        show_check.pack(side=tk.RIGHT)
        
        # Analyze button
        analyze_btn = tk.Button(
            input_frame,
            text="🔍 Analyze Password",
            command=self.analyze_password,
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        analyze_btn.pack(pady=(10, 0))
        
        # Results section
        results_frame = tk.LabelFrame(
            main_frame,
            text="Analysis Results",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50',
            padx=15,
            pady=15
        )
        results_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Score and category display
        score_frame = tk.Frame(results_frame, bg='#f0f0f0')
        score_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.score_label = tk.Label(
            score_frame,
            text="Score: --/100",
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        self.score_label.pack(side=tk.LEFT)
        
        self.category_label = tk.Label(
            score_frame,
            text="Category: --",
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        self.category_label.pack(side=tk.RIGHT)
        
        # Progress bar for score
        self.progress_bar = ttk.Progressbar(
            results_frame,
            length=400,
            mode='determinate',
            maximum=100
        )
        self.progress_bar.pack(fill=tk.X, pady=(0, 15))
        
        # Detailed results in notebook (tabs)
        notebook = ttk.Notebook(results_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Overview tab
        overview_frame = tk.Frame(notebook, bg='white')
        notebook.add(overview_frame, text="Overview")
        self.overview_text = scrolledtext.ScrolledText(
            overview_frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            bg='white',
            fg='#2c3e50',
            padx=10,
            pady=10
        )
        self.overview_text.pack(fill=tk.BOTH, expand=True)
        
        # Details tab
        details_frame = tk.Frame(notebook, bg='white')
        notebook.add(details_frame, text="Detailed Analysis")
        self.details_text = scrolledtext.ScrolledText(
            details_frame,
            wrap=tk.WORD,
            font=('Consolas', 9),
            bg='white',
            fg='#2c3e50',
            padx=10,
            pady=10
        )
        self.details_text.pack(fill=tk.BOTH, expand=True)
        
        # Recommendations tab
        rec_frame = tk.Frame(notebook, bg='white')
        notebook.add(rec_frame, text="Recommendations")
        self.rec_text = scrolledtext.ScrolledText(
            rec_frame,
            wrap=tk.WORD,
            font=('Arial', 10),
            bg='white',
            fg='#2c3e50',
            padx=10,
            pady=10
        )
        self.rec_text.pack(fill=tk.BOTH, expand=True)
        
        # Export buttons
        export_frame = tk.Frame(main_frame, bg='#f0f0f0')
        export_frame.pack(fill=tk.X)
        
        export_json_btn = tk.Button(
            export_frame,
            text="💾 Export JSON",
            command=lambda: self.export_report('json'),
            font=('Arial', 10),
            bg='#27ae60',
            fg='white',
            activebackground='#229954',
            padx=15,
            pady=8,
            cursor='hand2'
        )
        export_json_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        export_txt_btn = tk.Button(
            export_frame,
            text="📄 Export Text",
            command=lambda: self.export_report('txt'),
            font=('Arial', 10),
            bg='#27ae60',
            fg='white',
            activebackground='#229954',
            padx=15,
            pady=8,
            cursor='hand2'
        )
        export_txt_btn.pack(side=tk.LEFT)
        
        # Status bar
        self.status_label = tk.Label(
            self.root,
            text="Ready - Enter a password to analyze",
            font=('Arial', 9),
            bg='#34495e',
            fg='white',
            anchor=tk.W,
            padx=10,
            pady=5
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.current_report = None
    
    def toggle_password_visibility(self):
        """Toggle password visibility."""
        if self.show_password_var.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
    
    def on_password_change(self, *args):
        """Called when password changes."""
        # Auto-analyze on change (optional - can be removed if too resource-intensive)
        pass
    
    def analyze_password(self):
        """Analyze the entered password."""
        password = self.password_var.get()
        
        if not password:
            messagebox.showwarning("Warning", "Please enter a password to analyze.")
            return
        
        try:
            self.status_label.config(text="Analyzing password...")
            self.root.update()
            
            # Perform analysis
            report = self.checker.analyze(password)
            self.current_report = report
            
            # Update UI
            self.update_display(report)
            
            self.status_label.config(text="Analysis complete!")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text="Error during analysis")
    
    def update_display(self, report: dict):
        """Update the display with analysis results."""
        # Update score and category
        score = report['score']
        category = report['category']
        
        self.score_label.config(text=f"Score: {score:.1f}/100")
        self.category_label.config(text=f"Category: {category}")
        
        # Update progress bar with color
        self.progress_bar['value'] = score
        self.update_progress_color(score)
        
        # Update overview tab
        self.overview_text.delete(1.0, tk.END)
        overview_content = self.format_overview(report)
        self.overview_text.insert(1.0, overview_content)
        
        # Update details tab
        self.details_text.delete(1.0, tk.END)
        details_content = self.format_details(report)
        self.details_text.insert(1.0, details_content)
        
        # Update recommendations tab
        self.rec_text.delete(1.0, tk.END)
        rec_content = self.format_recommendations(report)
        self.rec_text.insert(1.0, rec_content)
    
    def update_progress_color(self, score: float):
        """Update progress bar color based on score."""
        if score < 30:
            style = 'red.Horizontal.TProgressbar'
        elif score < 50:
            style = 'orange.Horizontal.TProgressbar'
        elif score < 70:
            style = 'yellow.Horizontal.TProgressbar'
        elif score < 90:
            style = 'lightgreen.Horizontal.TProgressbar'
        else:
            style = 'green.Horizontal.TProgressbar'
        
        # Configure progress bar style
        s = ttk.Style()
        s.theme_use('clam')
        
        color_map = {
            'red': '#e74c3c',
            'orange': '#f39c12',
            'yellow': '#f1c40f',
            'lightgreen': '#2ecc71',
            'green': '#27ae60'
        }
        
        for name, color in color_map.items():
            s.configure(f'{name}.Horizontal.TProgressbar',
                       background=color,
                       troughcolor='#ecf0f1',
                       borderwidth=0,
                       lightcolor=color,
                       darkcolor=color)
        
        self.progress_bar.config(style=style)
    
    def format_overview(self, report: dict) -> str:
        """Format overview content."""
        lines = [
            "PASSWORD STRENGTH OVERVIEW",
            "=" * 50,
            "",
            f"Password Length: {report['length']} characters",
            f"Entropy: {report['entropy_bits']} bits",
            f"Strength Score: {report['score']:.2f}/100",
            f"Category: {report['category']}",
            "",
            "CRACKING TIME ESTIMATES:",
            "-" * 50,
            f"Online Brute-Force:  {report['cracking_time'].get('online_brute_force', 'N/A')}",
            f"Offline CPU Attack:  {report['cracking_time'].get('offline_cpu', 'N/A')}",
            f"Offline GPU Attack:  {report['cracking_time'].get('offline_gpu', 'N/A')}",
            f"Cloud Cracking:      {report['cracking_time'].get('cloud_cracking', 'N/A')}",
            "",
            "CHARACTER COMPOSITION:",
            "-" * 50,
        ]
        
        ca = report.get('character_analysis', {})
        lines.extend([
            f"✓ Lowercase letters: {ca.get('lowercase_count', 0)}",
            f"✓ Uppercase letters: {ca.get('uppercase_count', 0)}",
            f"✓ Digits:            {ca.get('digit_count', 0)}",
            f"✓ Special symbols:   {ca.get('symbol_count', 0)}",
            f"Character set size:  {ca.get('character_set_size', 0)}",
        ])
        
        return "\n".join(lines)
    
    def format_details(self, report: dict) -> str:
        """Format detailed analysis content."""
        lines = [
            "DETAILED PASSWORD ANALYSIS",
            "=" * 60,
            "",
            "PATTERNS DETECTED:",
            "-" * 60,
        ]
        
        patterns = report.get('patterns_detected', {})
        pattern_found = False
        
        for pattern_type, pattern_list in patterns.items():
            if pattern_list:
                pattern_found = True
                lines.append(f"\n{pattern_type.replace('_', ' ').title()}:")
                for pattern in pattern_list:
                    lines.append(f"  • {pattern}")
        
        if not pattern_found:
            lines.append("✓ No weak patterns detected")
        
        lines.append("")
        lines.append("DICTIONARY CHECK:")
        lines.append("-" * 60)
        
        dc = report.get('dictionary_check', {})
        if dc.get('is_common_password'):
            lines.append("⚠️  WARNING: This is a common password!")
        if dc.get('contains_dictionary_word'):
            words = dc.get('dictionary_words_found', [])
            lines.append(f"⚠️  Dictionary words found: {', '.join(words)}")
        if dc.get('contains_substituted_word'):
            lines.append("⚠️  Character substitution detected (e.g., @ for a)")
        if not any([dc.get('is_common_password'), dc.get('contains_dictionary_word'),
                   dc.get('contains_substituted_word')]):
            lines.append("✓ No dictionary words detected")
        
        lines.append("")
        lines.append("ENTROPY ANALYSIS:")
        lines.append("-" * 60)
        lines.append(f"Entropy: {report['entropy_bits']} bits")
        lines.append(f"Possible combinations: {report['cracking_time'].get('combinations', 'N/A')}")
        
        return "\n".join(lines)
    
    def format_recommendations(self, report: dict) -> str:
        """Format recommendations content."""
        lines = [
            "SECURITY RECOMMENDATIONS",
            "=" * 60,
            "",
        ]
        
        recommendations = report.get('recommendations', [])
        if recommendations:
            for i, rec in enumerate(recommendations, 1):
                lines.append(f"{i}. {rec}")
        else:
            lines.append("No specific recommendations. Password appears strong!")
        
        lines.append("")
        lines.append("GENERAL PASSWORD SECURITY TIPS:")
        lines.append("-" * 60)
        lines.extend([
            "• Use unique passwords for each account",
            "• Never share your passwords with anyone",
            "• Consider using a password manager",
            "• Enable two-factor authentication when available",
            "• Change passwords if you suspect a breach",
            "• Avoid using personal information (names, dates, etc.)",
            "• Use passphrases for better memorability and security"
        ])
        
        return "\n".join(lines)
    
    def export_report(self, format_type: str):
        """Export report to file."""
        if not self.current_report:
            messagebox.showwarning("Warning", "Please analyze a password first.")
            return
        
        # Get filename from user
        if format_type == 'json':
            filename = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
        else:
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
        
        if filename:
            try:
                self.checker.export_report(self.current_report, filename, format_type)
                messagebox.showinfo("Success", f"Report exported successfully to:\n{filename}")
                self.status_label.config(text=f"Report exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export report: {str(e)}")


def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    app = PasswordStrengthGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

