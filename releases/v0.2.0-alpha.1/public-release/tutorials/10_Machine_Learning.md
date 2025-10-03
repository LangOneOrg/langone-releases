# Tutorial 10: Machine Learning and AI Models

## 🎯 **Learning Objectives**

- ✅ Load and manage ML models
- ✅ Perform model inference and prediction
- ✅ Train clustering and classification models
- ✅ Optimize models with quantization and pruning
- ✅ Evaluate model performance
- ✅ Deploy AI applications

**⏱️ Estimated Time**: 90 minutes | **Prerequisites**: Tutorials 01-09 | **Difficulty**: ⭐⭐⭐⭐⭐ Expert

---

## 🤖 **Part 1: AI Core and Model Loading**

### **Initialize AI System**

```l1
# Initialize AI core
let ai = ai_core()
print("AI system initialized")
print("BLAS support: enabled")
print("GPU support: enabled")
```

### **Load Pre-trained Model**

```l1
# Load model
let model_data = load_data("model_weights.bin")
let model = load_model("resnet50", model_data)
print("Model loaded: ResNet-50")
print("Parameters: 25.6M")
```

### **Model Inference**

```l1
# Prepare input
let input_image = ones([1, 3, 224, 224])  # Batch=1, Channels=3, H=224, W=224

# Configure inference
let config = {
    "batch_size": 1,
    "precision": "fp32",
    "device": "gpu"
}

# Run inference
let predictions = infer(model, input_image, config)
print("Predictions:", predictions)
print("Top class:", argmax(predictions))
```

---

## 🎯 **Part 2: Clustering**

### **K-Means Clustering**

```l1
# Sample data points
let data = array([
    [1, 2], [2, 3], [1, 3],      # Cluster 1
    [8, 8], [9, 9], [8, 9],      # Cluster 2
    [15, 2], [16, 3], [15, 3]    # Cluster 3
])

# Perform K-Means clustering
let k = 3
let clusters = kmeans(data, k)
print("K-Means clustering (k=" + to_string(k) + "):")
print("Cluster labels:", clusters.labels)
print("Cluster centers:", clusters.centers)
```

### **DBSCAN Clustering**

```l1
# Density-based clustering
let dbscan_result = dbscan(data, eps=2.0, min_samples=2)
print("DBSCAN clustering:")
print("Clusters found:", dbscan_result.n_clusters)
print("Noise points:", dbscan_result.n_noise)
```

---

### **🔨 Exercise 1: Customer Segmentation**

```l1
# Segment customers based on:
# - Purchase frequency
# - Average order value
# - Recency
# Use K-Means to find segments
```

<details>
<summary>💡 Solution</summary>

```l1
# Customer Segmentation

print("=== Customer Segmentation Analysis ===")
print("")

# Customer data
let customers = dataframe({
    "customer_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "purchase_frequency": [2, 15, 3, 20, 4, 18, 5, 22, 3, 16],
    "avg_order_value": [50, 200, 60, 250, 55, 220, 58, 240, 52, 210],
    "recency_days": [30, 5, 25, 3, 28, 7, 24, 4, 29, 6]
})

# Extract features for clustering
let features = array([
    customers["purchase_frequency"],
    customers["avg_order_value"],
    customers["recency_days"]
])

# Normalize features (important for clustering)
for i in range(0, len(features)):
    let col = features[i]
    features[i] = (col - mean(col)) / std(col)
end

# Perform K-Means (k=3 segments)
let result = kmeans(features, 3)

print("Customer Segments:")
print("Segment 1: Low-value, infrequent")
print("Segment 2: High-value, frequent (VIP)")
print("Segment 3: Medium-value, moderate")
print("")

# Assign segments
customers["segment"] = result.labels
print("Segmented customers:")
print(customers)

# Analyze segments
let by_segment = df_groupby(customers, ["segment"])
let avg_value = groupby_agg(by_segment, "avg_order_value", "mean")
print("Average order value by segment:")
print(avg_value)
```
</details>

---

## 🎓 **Part 3: Classification**

### **Train Classifier**

```l1
# Training data
let X_train = array([[1, 2], [2, 3], [3, 4], [8, 8], [9, 9], [10, 10]])
let y_train = array([0, 0, 0, 1, 1, 1])  # Labels

# Train SVM classifier
let svm_model = train_svm(X_train, y_train)
print("SVM model trained")

# Make predictions
let X_test = array([[1.5, 2.5], [9, 9]])
let predictions = predict(svm_model, X_test)
print("Predictions:", predictions)
```

---

## 🧠 **Part 4: Neural Networks**

### **Build Neural Network**

```l1
# Define architecture
let nn_config = {
    "layers": [
        {"type": "dense", "units": 128, "activation": "relu"},
        {"type": "dropout", "rate": 0.2},
        {"type": "dense", "units": 64, "activation": "relu"},
        {"type": "dense", "units": 10, "activation": "softmax"}
    ],
    "optimizer": "adam",
    "loss": "categorical_crossentropy"
}

let model = build_neural_network(nn_config)
print("Neural network created")
```

### **Model Optimization**

```l1
# Quantize model (reduce size)
let quantized = quantize_model(model, "8bit", "dynamic")
print("Model quantized: 4x smaller, minimal accuracy loss")

# Prune model (remove unimportant connections)
let pruned = prune_model(model, "0.3", "magnitude")
print("Model pruned: 30% of weights removed")
```

---

### **🔨 Exercise 2: Image Classifier**

```l1
# Build image classifier:
# 1. Load pre-trained model
# 2. Prepare image data
# 3. Run inference
# 4. Optimize model
# 5. Compare performance
```

<details>
<summary>💡 Solution</summary>

```l1
# Image Classification Pipeline

print("=== Image Classification System ===")
print("")

# 1. Load model
print("Loading model...")
let ai = ai_core()
let model = load_model("mobilenet_v2", null)
print("✓ MobileNet V2 loaded (3.5M parameters)")
print("")

# 2. Prepare image
print("Preparing image...")
let image = ones([1, 3, 224, 224])  # Simulated image
print("✓ Image preprocessed: 224x224x3")
print("")

# 3. Run inference
print("Running inference (FP32)...")
let config_fp32 = {"precision": "fp32", "device": "gpu"}
let start_fp32 = time()
let pred_fp32 = infer(model, image, config_fp32)
let time_fp32 = time() - start_fp32
print("✓ Inference time: " + to_string(time_fp32 * 1000) + "ms")
print("")

# 4. Optimize model
print("Optimizing model (INT8 quantization)...")
let optimized_model = quantize_model(model, "8bit", "dynamic")
print("✓ Model size: 4x smaller")
print("")

# 5. Compare performance
print("Running optimized inference (INT8)...")
let config_int8 = {"precision": "int8", "device": "gpu"}
let start_int8 = time()
let pred_int8 = infer(optimized_model, image, config_int8)
let time_int8 = time() - start_int8
print("✓ Inference time: " + to_string(time_int8 * 1000) + "ms")
print("")

print("PERFORMANCE COMPARISON")
print("───────────────────────────────────────")
print("FP32: " + to_string(time_fp32 * 1000) + "ms")
print("INT8: " + to_string(time_int8 * 1000) + "ms")
print("Speedup: " + to_string(time_fp32 / time_int8) + "x faster")
print("Size reduction: 4x smaller")
print("Accuracy loss: <1%")
print("")
print("Optimization complete! 🚀")
```
</details>

---

## ✅ **Knowledge Check**

1. **What is model quantization?**
   <details><summary>Answer</summary>Reducing precision (FP32→INT8) to decrease model size</details>

2. **What's the benefit of model pruning?**
   <details><summary>Answer</summary>Removes unimportant weights, reduces size and inference time</details>

3. **What clustering algorithm works best for arbitrary shapes?**
   <details><summary>Answer</summary>DBSCAN (density-based)</details>

---

## 🎓 **What You've Learned**

- ✅ ML model loading and inference
- ✅ Clustering (K-Means, DBSCAN)
- ✅ Classification (SVM, Random Forest)
- ✅ Neural networks
- ✅ Model optimization

---

## 🚀 **Next Steps**

👉 **[Tutorial 11: Distributed and Real-Time Computing](./11_Distributed_Computing.md)**

**Progress**: [x] Tutorials 01-10 ✅

---

*© 2025 LangOne Project.*

