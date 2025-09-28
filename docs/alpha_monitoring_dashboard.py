#!/usr/bin/env python3
"""
LangOne Alpha Phase Monitoring Dashboard
Real-time monitoring of alpha phase metrics and progress
"""

import json
import os
import requests
from datetime import datetime, timedelta
import time

class AlphaMonitoringDashboard:
    def __init__(self, repo_org="langone", repo_name="langone"):
        self.repo_org = repo_org
        self.repo_name = repo_name
        self.github_api = f"https://api.github.com/repos/{repo_org}/{repo_name}"
        self.metrics_file = "alpha_metrics.json"
        self.load_metrics()
    
    def load_metrics(self):
        """Load existing metrics from file"""
        if os.path.exists(self.metrics_file):
            with open(self.metrics_file, 'r') as f:
                self.metrics = json.load(f)
        else:
            self.metrics = {
                "installation_success": [],
                "sample_program_success": [],
                "active_testers": [],
                "bug_reports": [],
                "community_growth": [],
                "daily_updates": []
            }
    
    def save_metrics(self):
        """Save metrics to file"""
        with open(self.metrics_file, 'w') as f:
            json.dump(self.metrics, f, indent=2)
    
    def get_github_stats(self):
        """Get GitHub repository statistics"""
        try:
            # Get repository info
            repo_response = requests.get(self.github_api)
            repo_data = repo_response.json()
            
            # Get issues
            issues_response = requests.get(f"{self.github_api}/issues")
            issues_data = issues_response.json()
            
            # Get stars
            stars = repo_data.get('stargazers_count', 0)
            
            # Get forks
            forks = repo_data.get('forks_count', 0)
            
            # Get open issues
            open_issues = repo_data.get('open_issues_count', 0)
            
            return {
                "stars": stars,
                "forks": forks,
                "open_issues": open_issues,
                "total_issues": len(issues_data)
            }
        except Exception as e:
            print(f"Error fetching GitHub stats: {e}")
            return {
                "stars": 0,
                "forks": 0,
                "open_issues": 0,
                "total_issues": 0
            }
    
    def update_daily_metrics(self, installation_success, sample_program_success, active_testers, bug_reports):
        """Update daily metrics"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        daily_metric = {
            "date": today,
            "installation_success": installation_success,
            "sample_program_success": sample_program_success,
            "active_testers": active_testers,
            "bug_reports": bug_reports,
            "github_stats": self.get_github_stats()
        }
        
        # Add to metrics
        self.metrics["daily_updates"].append(daily_metric)
        
        # Keep only last 30 days
        if len(self.metrics["daily_updates"]) > 30:
            self.metrics["daily_updates"] = self.metrics["daily_updates"][-30:]
        
        self.save_metrics()
        return daily_metric
    
    def get_success_rate(self, metric_name):
        """Get success rate for a metric"""
        if not self.metrics["daily_updates"]:
            return 0
        
        recent_updates = self.metrics["daily_updates"][-7:]  # Last 7 days
        if not recent_updates:
            return 0
        
        total = sum(update.get(metric_name, 0) for update in recent_updates)
        return total / len(recent_updates) if recent_updates else 0
    
    def get_trend(self, metric_name):
        """Get trend for a metric (improving/stable/declining)"""
        if len(self.metrics["daily_updates"]) < 2:
            return "stable"
        
        recent = self.metrics["daily_updates"][-3:]  # Last 3 days
        if len(recent) < 2:
            return "stable"
        
        first = recent[0].get(metric_name, 0)
        last = recent[-1].get(metric_name, 0)
        
        if last > first * 1.05:  # 5% improvement
            return "improving"
        elif last < first * 0.95:  # 5% decline
            return "declining"
        else:
            return "stable"
    
    def print_dashboard(self):
        """Print the monitoring dashboard"""
        print("🔍 LangOne Alpha Phase Monitoring Dashboard")
        print("=" * 50)
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Repository: {self.repo_org}/{self.repo_name}")
        print()
        
        # Get current metrics
        if self.metrics["daily_updates"]:
            current = self.metrics["daily_updates"][-1]
            github_stats = current.get("github_stats", {})
        else:
            current = {}
            github_stats = {}
        
        # Installation Success
        installation_success = current.get("installation_success", 0)
        installation_trend = self.get_trend("installation_success")
        print(f"📊 Installation Success: {installation_success}% (Target: ≥90%)")
        print(f"   Trend: {installation_trend}")
        
        # Sample Program Success
        sample_success = current.get("sample_program_success", 0)
        sample_trend = self.get_trend("sample_program_success")
        print(f"📊 Sample Program Success: {sample_success}% (Target: ≥80%)")
        print(f"   Trend: {sample_trend}")
        
        # Active Testers
        active_testers = current.get("active_testers", 0)
        tester_trend = self.get_trend("active_testers")
        print(f"👥 Active Testers: {active_testers} (Target: ≥25)")
        print(f"   Trend: {tester_trend}")
        
        # Bug Reports
        bug_reports = current.get("bug_reports", 0)
        bug_trend = self.get_trend("bug_reports")
        print(f"🐛 Bug Reports: {bug_reports} (Target: ≤5 P0)")
        print(f"   Trend: {bug_trend}")
        
        # Community Growth
        stars = github_stats.get("stars", 0)
        forks = github_stats.get("forks", 0)
        issues = github_stats.get("open_issues", 0)
        print(f"⭐ GitHub Stars: {stars} (Target: ≥50)")
        print(f"🍴 Forks: {forks}")
        print(f"📝 Open Issues: {issues}")
        
        print()
        
        # Overall Status
        overall_status = self.get_overall_status()
        print(f"🎯 Overall Status: {overall_status}")
        
        # Risk Assessment
        risks = self.assess_risks()
        if risks:
            print(f"⚠️  Risks: {', '.join(risks)}")
        else:
            print("✅ No significant risks identified")
        
        print()
        
        # Next Actions
        actions = self.get_next_actions()
        if actions:
            print("📋 Next Actions:")
            for i, action in enumerate(actions, 1):
                print(f"   {i}. {action}")
        
        print()
    
    def get_overall_status(self):
        """Get overall alpha phase status"""
        if not self.metrics["daily_updates"]:
            return "Not Started"
        
        current = self.metrics["daily_updates"][-1]
        
        # Check success criteria
        installation_ok = current.get("installation_success", 0) >= 90
        sample_ok = current.get("sample_program_success", 0) >= 80
        testers_ok = current.get("active_testers", 0) >= 25
        bugs_ok = current.get("bug_reports", 0) <= 5
        
        if installation_ok and sample_ok and testers_ok and bugs_ok:
            return "🟢 On Track"
        elif installation_ok and sample_ok:
            return "🟡 Attention Needed"
        else:
            return "🔴 Action Required"
    
    def assess_risks(self):
        """Assess risks based on current metrics"""
        risks = []
        
        if not self.metrics["daily_updates"]:
            return risks
        
        current = self.metrics["daily_updates"][-1]
        
        if current.get("installation_success", 0) < 80:
            risks.append("Low installation success")
        
        if current.get("sample_program_success", 0) < 70:
            risks.append("Low sample program success")
        
        if current.get("active_testers", 0) < 20:
            risks.append("Low tester engagement")
        
        if current.get("bug_reports", 0) > 10:
            risks.append("High bug count")
        
        return risks
    
    def get_next_actions(self):
        """Get recommended next actions"""
        actions = []
        
        if not self.metrics["daily_updates"]:
            return ["Start alpha phase monitoring"]
        
        current = self.metrics["daily_updates"][-1]
        
        if current.get("installation_success", 0) < 90:
            actions.append("Improve installation success rate")
        
        if current.get("sample_program_success", 0) < 80:
            actions.append("Fix sample program issues")
        
        if current.get("active_testers", 0) < 25:
            actions.append("Increase tester engagement")
        
        if current.get("bug_reports", 0) > 5:
            actions.append("Resolve critical bugs")
        
        if not actions:
            actions.append("Continue monitoring and collecting feedback")
        
        return actions
    
    def run_interactive_dashboard(self):
        """Run interactive dashboard"""
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            self.print_dashboard()
            
            print("Options:")
            print("1. Update metrics")
            print("2. View historical data")
            print("3. Export report")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                self.update_metrics_interactive()
            elif choice == "2":
                self.view_historical_data()
            elif choice == "3":
                self.export_report()
            elif choice == "4":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")
    
    def update_metrics_interactive(self):
        """Update metrics interactively"""
        print("\n📊 Update Daily Metrics")
        print("=" * 25)
        
        try:
            installation_success = float(input("Installation success rate (%): "))
            sample_program_success = float(input("Sample program success rate (%): "))
            active_testers = int(input("Active testers count: "))
            bug_reports = int(input("Bug reports count: "))
            
            self.update_daily_metrics(
                installation_success,
                sample_program_success,
                active_testers,
                bug_reports
            )
            
            print("✅ Metrics updated successfully!")
            
        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")
    
    def view_historical_data(self):
        """View historical data"""
        print("\n📈 Historical Data")
        print("=" * 20)
        
        if not self.metrics["daily_updates"]:
            print("No historical data available.")
            return
        
        print(f"{'Date':<12} {'Install':<8} {'Sample':<8} {'Testers':<8} {'Bugs':<6}")
        print("-" * 50)
        
        for update in self.metrics["daily_updates"][-10:]:  # Last 10 days
            date = update.get("date", "Unknown")
            install = update.get("installation_success", 0)
            sample = update.get("sample_program_success", 0)
            testers = update.get("active_testers", 0)
            bugs = update.get("bug_reports", 0)
            
            print(f"{date:<12} {install:<8} {sample:<8} {testers:<8} {bugs:<6}")
    
    def export_report(self):
        """Export monitoring report"""
        report_file = f"alpha_monitoring_report_{datetime.now().strftime('%Y%m%d')}.json"
        
        with open(report_file, 'w') as f:
            json.dump(self.metrics, f, indent=2)
        
        print(f"✅ Report exported to {report_file}")

def main():
    """Main function"""
    dashboard = AlphaMonitoringDashboard()
    
    print("🚀 LangOne Alpha Phase Monitoring Dashboard")
    print("=" * 50)
    print("Starting monitoring dashboard...")
    print()
    
    # Print initial dashboard
    dashboard.print_dashboard()
    
    # Ask if user wants to run interactively
    choice = input("Run interactive dashboard? (y/N): ")
    if choice.lower() == 'y':
        dashboard.run_interactive_dashboard()
    else:
        print("Dashboard ready. Use 'python3 alpha_monitoring_dashboard.py' to run interactively.")

if __name__ == "__main__":
    main()
