# Tutorial 12: Data Visualization and Dashboards

## 🎯 **Learning Objectives**

- ✅ Create interactive charts (line, bar, scatter, pie)
- ✅ Build 3D visualizations and surface plots
- ✅ Design real-time updating dashboards
- ✅ Export visualizations to multiple formats
- ✅ Apply visualization best practices
- ✅ Build professional data presentations

**⏱️ Estimated Time**: 75 minutes | **Prerequisites**: Tutorials 01-09 | **Difficulty**: ⭐⭐⭐⭐☆ Advanced

---

## 📚 **Introduction: Visual Data Communication**

"A picture is worth a thousand numbers." Visualization transforms data into insights:
- **📊 Understanding**: See patterns instantly
- **📈 Communication**: Present findings effectively
- **🎯 Decision Making**: Guide business decisions
- **🔍 Exploration**: Discover hidden insights

---

## 📊 **Part 1: Basic Charts**

### **Line Chart**

```l1
# Create line chart
let x = linspace(0, 10, 100)
let y = sin(x)

let chart = create_chart("line", {
    "x": x,
    "y": y,
    "title": "Sine Wave",
    "xlabel": "Time",
    "ylabel": "Amplitude"
})

save_chart(chart, "sine_wave.png")
print("Line chart created")
```

### **Bar Chart**

```l1
# Sales by product
let products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
let sales = [1200, 250, 180, 850]

let bar_chart = create_chart("bar", {
    "x": products,
    "y": sales,
    "title": "Product Sales",
    "xlabel": "Product",
    "ylabel": "Revenue ($)"
})

save_chart(bar_chart, "sales_bar.png")
```

### **Scatter Plot**

```l1
# Correlation analysis
let height = array([150, 160, 165, 170, 175, 180, 185, 190])
let weight = array([50, 60, 65, 70, 75, 80, 85, 90])

let scatter = create_chart("scatter", {
    "x": height,
    "y": weight,
    "title": "Height vs Weight",
    "xlabel": "Height (cm)",
    "ylabel": "Weight (kg)"
})

save_chart(scatter, "height_weight.png")
```

### **Pie Chart**

```l1
# Market share
let companies = ["CompanyA", "CompanyB", "CompanyC", "Others"]
let market_share = [35, 28, 22, 15]

let pie = create_chart("pie", {
    "labels": companies,
    "values": market_share,
    "title": "Market Share 2025"
})

save_chart(pie, "market_share.png")
```

---

### **🔨 Exercise 1: Sales Dashboard**

```l1
# Create multi-chart dashboard:
# 1. Monthly revenue trend (line chart)
# 2. Sales by category (bar chart)
# 3. Regional distribution (pie chart)
# 4. Export all charts
```

<details>
<summary>💡 Solution</summary>

```l1
# Sales Dashboard

print("=== Sales Dashboard Creation ===")
print("")

# Data preparation
let months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
let revenue = [45000, 52000, 48000, 61000, 58000, 67000]

let categories = ["Electronics", "Clothing", "Food", "Books"]
let category_sales = [125000, 98000, 145000, 67000]

let regions = ["North", "South", "East", "West"]
let regional_sales = [98000, 112000, 87000, 138000]

# 1. Monthly revenue trend
print("Creating revenue trend chart...")
let trend_chart = create_chart("line", {
    "x": months,
    "y": revenue,
    "title": "Monthly Revenue Trend",
    "xlabel": "Month",
    "ylabel": "Revenue ($)",
    "color": "blue",
    "line_width": 2
})
save_chart(trend_chart, "revenue_trend.png")
print("✓ Trend chart saved")

# 2. Category sales
print("Creating category sales chart...")
let category_chart = create_chart("bar", {
    "x": categories,
    "y": category_sales,
    "title": "Sales by Category",
    "xlabel": "Category",
    "ylabel": "Sales ($)",
    "color": "green"
})
save_chart(category_chart, "category_sales.png")
print("✓ Category chart saved")

# 3. Regional distribution
print("Creating regional distribution chart...")
let regional_chart = create_chart("pie", {
    "labels": regions,
    "values": regional_sales,
    "title": "Regional Sales Distribution",
    "colors": ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0"]
})
save_chart(regional_chart, "regional_distribution.png")
print("✓ Regional chart saved")

print("")
print("Dashboard complete! All charts exported ✓")
```
</details>

---

## 🎨 **Part 2: 3D Visualizations**

### **3D Surface Plot**

```l1
# Create 3D surface
let x = linspace(-5, 5, 50)
let y = linspace(-5, 5, 50)
let z = []

# Calculate z values for surface
for xi in x:
    let row = []
    for yi in y:
        let z_val = sin(sqrt(xi**2 + yi**2))
        row.append(z_val)
    end
    z.append(row)
end

let surface = create_3d_plot("surface", {
    "x": x,
    "y": y,
    "z": z,
    "title": "3D Surface Plot",
    "colormap": "viridis"
})

save_chart(surface, "surface_plot.png")
```

### **3D Scatter Plot**

```l1
# 3D point cloud
let x = array([1, 2, 3, 4, 5])
let y = array([2, 4, 6, 8, 10])
let z = array([1, 4, 9, 16, 25])

let scatter_3d = create_3d_plot("scatter", {
    "x": x,
    "y": y,
    "z": z,
    "title": "3D Scatter Plot",
    "marker_size": 10
})

save_chart(scatter_3d, "scatter_3d.png")
```

---

## 📱 **Part 3: Interactive Dashboards**

### **Create Dashboard**

```l1
# Initialize dashboard
let dashboard = create_dashboard("Sales Analytics", {
    "layout": "grid",
    "columns": 2,
    "refresh_interval": "5s"
})

# Add charts
dashboard.add_chart("revenue_trend", trend_chart, position=[0, 0])
dashboard.add_chart("category_sales", category_chart, position=[0, 1])
dashboard.add_chart("regional_dist", regional_chart, position=[1, 0])

# Add real-time metrics
dashboard.add_metric("total_sales", {
    "value": 435000,
    "label": "Total Sales",
    "format": "currency"
})

dashboard.add_metric("growth", {
    "value": 15.3,
    "label": "Growth Rate",
    "format": "percentage"
})

# Start dashboard
dashboard.start()
print("Dashboard running at http://localhost:8080")
```

---

### **🔨 Exercise 2: Analytics Dashboard**

```l1
# Build complete analytics dashboard:
# 1. Revenue trends over time
# 2. Product performance comparison
# 3. Geographic sales map
# 4. Real-time metrics (sales, orders, avg order value)
# 5. Interactive filters
```

<details>
<summary>💡 Solution</summary>

```l1
# Complete Analytics Dashboard

print("=== Building Analytics Dashboard ===")
print("")

# Initialize dashboard
let dashboard = create_dashboard("Executive Sales Dashboard", {
    "layout": "grid",
    "columns": 3,
    "theme": "dark",
    "refresh_interval": "10s"
})

print("Dashboard initialized")
print("")

# Prepare data
let dates = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06"]
let monthly_revenue = [145000, 152000, 148000, 161000, 168000, 175000]
let monthly_orders = [1250, 1310, 1280, 1390, 1450, 1520]

# 1. Revenue trend
print("Adding revenue trend chart...")
let revenue_chart = create_chart("line", {
    "x": dates,
    "y": monthly_revenue,
    "title": "Monthly Revenue Trend",
    "color": "#00ff00"
})
dashboard.add_chart("revenue", revenue_chart, [0, 0])

# 2. Product performance
print("Adding product performance...")
let products = ["Product A", "Product B", "Product C", "Product D"]
let product_sales = [285000, 198000, 145000, 87000]
let product_chart = create_chart("bar", {
    "x": products,
    "y": product_sales,
    "title": "Product Performance"
})
dashboard.add_chart("products", product_chart, [0, 1])

# 3. Geographic distribution
print("Adding geographic sales...")
let regions = ["North America", "Europe", "Asia", "Others"]
let regional_revenue = [320000, 245000, 178000, 72000]
let geo_chart = create_chart("pie", {
    "labels": regions,
    "values": regional_revenue,
    "title": "Sales by Region"
})
dashboard.add_chart("geography", geo_chart, [0, 2])

# 4. Real-time metrics
print("Adding real-time metrics...")
dashboard.add_metric("total_revenue", {
    "value": sum(monthly_revenue),
    "label": "Total Revenue",
    "format": "currency",
    "position": [1, 0]
})

dashboard.add_metric("total_orders", {
    "value": sum(monthly_orders),
    "label": "Total Orders",
    "format": "number",
    "position": [1, 1]
})

let avg_order = sum(monthly_revenue) / sum(monthly_orders)
dashboard.add_metric("avg_order_value", {
    "value": avg_order,
    "label": "Avg Order Value",
    "format": "currency",
    "position": [1, 2]
})

# Export dashboard
print("")
print("Exporting dashboard...")
export_dashboard(dashboard, "sales_dashboard.html")
print("✓ Dashboard exported to sales_dashboard.html")
print("")

print("Dashboard creation complete! 📊")
print("Open sales_dashboard.html in your browser")
```
</details>

---

## ✅ **Knowledge Check**

1. **What chart type is best for showing trends over time?**
   <details><summary>Answer</summary>Line chart</details>

2. **When should you use a pie chart?**
   <details><summary>Answer</summary>To show parts of a whole (percentages)</details>

3. **What's the advantage of interactive dashboards?**
   <details><summary>Answer</summary>Real-time updates, user interaction, dynamic filtering</details>

4. **What format is best for web dashboards?**
   <details><summary>Answer</summary>HTML with interactive JavaScript</details>

---

## 🎓 **What You've Learned**

- ✅ Creating various chart types
- ✅ Building 3D visualizations
- ✅ Designing interactive dashboards
- ✅ Exporting to multiple formats
- ✅ Real-time data presentation
- ✅ Visualization best practices

---

## 🚀 **Next Steps**

**Practice Projects:**
1. Build stock market dashboard
2. Create weather visualization system
3. Design ML model performance dashboard

👉 **[Tutorial 13: Performance Optimization and Profiling](./13_Performance_Optimization.md)**

**Progress**: [x] Tutorials 01-12 ✅

---

*© 2025 LangOne Project.*

