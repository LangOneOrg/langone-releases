# Tutorial 11: Distributed and Real-Time Computing

## 🎯 **Learning Objectives**

- ✅ Set up and manage distributed clusters
- ✅ Execute parallel processing across nodes
- ✅ Implement load balancing strategies
- ✅ Handle fault tolerance and recovery
- ✅ Process real-time data streams
- ✅ Build scalable distributed applications

**⏱️ Estimated Time**: 90 minutes | **Prerequisites**: Tutorials 01-10 | **Difficulty**: ⭐⭐⭐⭐⭐ Expert

---

## 📚 **Introduction: Scaling Beyond Single Machines**

When data and computations exceed a single machine's capacity, distributed computing becomes essential:
- **📊 Big Data**: Process terabytes of data
- **⚡ High Performance**: Parallel execution across nodes
- **🔄 Fault Tolerance**: Automatic recovery from failures
- **🌐 Scalability**: Add nodes as needed

---

## 🖥️ **Part 1: Cluster Computing**

### **Initialize Distributed Cluster**

```l1
# Initialize distributed computing cluster
let cluster = distributed_init()
print("Distributed cluster initialized")
print("Cluster ID: " + cluster.id)
```

### **Add Nodes to Cluster**

```l1
# Add compute nodes
let node1 = cluster_add_node("node-1:192.168.1.10:4:8192")
print("Node 1 added: 4 CPUs, 8GB RAM")

let node2 = cluster_add_node("node-2:192.168.1.11:8:16384")
print("Node 2 added: 8 CPUs, 16GB RAM")

let node3 = cluster_add_node("node-3:192.168.1.12:16:32768")
print("Node 3 added: 16 CPUs, 32GB RAM")

# Get cluster status
let status = cluster_status()
print("Cluster Status:")
print("Total Nodes: " + to_string(status.total_nodes))
print("Online Nodes: " + to_string(status.online_nodes))
print("Cluster Utilization: " + to_string(status.utilization) + "%")
```

---

### **🔨 Exercise 1: Cluster Setup**

```l1
# Set up a 3-node cluster:
# 1. Initialize cluster
# 2. Add nodes with different capacities
# 3. Check cluster health
# 4. Display resource availability
```

<details>
<summary>💡 Solution</summary>

```l1
# Cluster Setup and Configuration

print("=== Distributed Cluster Setup ===")
print("")

# 1. Initialize cluster
let cluster = distributed_init()
print("Step 1: Cluster initialized")
print("Cluster ID: " + cluster.id)
print("")

# 2. Add nodes
print("Step 2: Adding compute nodes...")
let nodes = [
    cluster_add_node("worker-1:10.0.0.10:4:8192:IT"),
    cluster_add_node("worker-2:10.0.0.11:8:16384:Analytics"),
    cluster_add_node("worker-3:10.0.0.12:16:32768:ML")
]
print("✓ Added 3 nodes")
print("")

# 3. Check cluster health
print("Step 3: Checking cluster health...")
let status = cluster_status()
print("✓ Total Nodes: " + to_string(status.total_nodes))
print("✓ Online Nodes: " + to_string(status.online_nodes))
print("✓ Health Status: " + (status.online_nodes == status.total_nodes ? "Healthy" : "Degraded"))
print("")

# 4. Display resources
print("Step 4: Resource Availability")
print("───────────────────────────────────────")
let total_cpus = 4 + 8 + 16
let total_memory = 8192 + 16384 + 32768
print("Total CPUs: " + to_string(total_cpus) + " cores")
print("Total Memory: " + to_string(total_memory / 1024) + " GB")
print("Cluster Utilization: " + to_string(status.utilization) + "%")
print("")
print("Cluster ready for workload! ✓")
```
</details>

---

## ⚡ **Part 2: Parallel Processing**

### **Submit Tasks to Cluster**

```l1
# Submit computational tasks
let task1 = cluster_submit_task("task-1:script:process_data.l1:[]:node-1:3:300")
print("Task 1 submitted to node-1")

let task2 = cluster_submit_task("task-2:function:calculate_stats:[]:node-2:5:600")
print("Task 2 submitted to node-2")

let task3 = cluster_submit_task("task-3:data:analyze_dataset:[]:node-3:2:180")
print("Task 3 submitted to node-3")

# Monitor task execution
let task_status = cluster_task_status("task-1")
print("Task 1 status:", task_status.status)
```

### **Parallel Data Processing**

```l1
# Process large dataset in parallel
let large_dataset = arange(0, 1000000)

# Split into chunks for parallel processing
let chunk_size = 250000
let tasks = []

for i in range(0, len(large_dataset), chunk_size):
    let chunk = large_dataset[i:i + chunk_size]
    let task = cluster_submit_task("process_chunk", chunk)
    tasks.append(task)
end

# Wait for all tasks to complete
let results = cluster_wait_all(tasks)
print("All tasks completed")

# Combine results
let final_result = concatenate(results)
print("Final result size: " + to_string(len(final_result)))
```

---

### **🔨 Exercise 2: Distributed Data Analysis**

```l1
# Distribute analysis across cluster:
# 1. Load large dataset
# 2. Split into partitions
# 3. Process each partition on different node
# 4. Aggregate results
# 5. Generate summary report
```

<details>
<summary>💡 Solution</summary>

```l1
# Distributed Data Analysis Pipeline

print("=== Distributed Data Analysis ===")
print("")

# 1. Load large dataset
print("Loading dataset...")
let dataset = read_csv("large_sales_data.csv")
print("✓ Loaded " + to_string(len(dataset)) + " records")
print("")

# 2. Split into partitions
print("Partitioning data...")
let num_partitions = 3
let partition_size = len(dataset) / num_partitions
let partitions = []

for i in range(0, num_partitions):
    let start_idx = i * partition_size
    let end_idx = (i + 1) * partition_size
    let partition = dataset[start_idx:end_idx]
    partitions.append(partition)
end
print("✓ Created " + to_string(num_partitions) + " partitions")
print("")

# 3. Submit tasks to cluster
print("Submitting tasks to cluster...")
let tasks = []
for i in range(0, num_partitions):
    let task_id = "analysis-partition-" + to_string(i)
    let task = cluster_submit_task(task_id + ":data:analyze:[]:auto:3:600")
    tasks.append(task)
end
print("✓ " + to_string(len(tasks)) + " tasks submitted")
print("")

# 4. Wait for completion and aggregate
print("Processing in parallel...")
let results = cluster_wait_all(tasks)
print("✓ All tasks completed")
print("")

# Aggregate results
let total_revenue = 0
let total_transactions = 0
for result in results:
    total_revenue = total_revenue + result.revenue
    total_transactions = total_transactions + result.count
end

# 5. Generate report
print("ANALYSIS RESULTS")
print("───────────────────────────────────────")
print("Total Transactions: " + to_string(total_transactions))
print("Total Revenue: $" + to_string(total_revenue))
print("Average Transaction: $" + to_string(total_revenue / total_transactions))
print("")
print("Distributed analysis complete! ✓")
```
</details>

---

## 🌊 **Part 3: Real-Time Stream Processing**

### **Initialize Stream Processor**

```l1
# Create real-time stream processor
let stream_config = {
    "buffer_size": 10000,
    "window_size": "5s",
    "watermark_delay": "1s"
}

let stream = create_stream("sensor_data", stream_config)
print("Stream processor initialized")
```

### **Process Streaming Data**

```l1
# Process data stream
while (stream.is_active()) {
    # Get next batch
    let batch = stream.next_batch()
    
    # Process batch
    let avg_value = mean(batch["value"])
    let max_value = max(batch["value"])
    
    # Check for anomalies
    if (max_value > threshold) {
        emit_alert("High value detected: " + to_string(max_value))
    }
    
    # Update dashboard
    update_dashboard(avg_value, max_value)
}
```

---

### **🔨 Exercise 3: Real-Time Monitoring System**

```l1
# Build real-time monitoring:
# 1. Stream sensor data
# 2. Calculate rolling averages
# 3. Detect anomalies
# 4. Send alerts
# 5. Update dashboard
```

<details>
<summary>💡 Solution</summary>

```l1
# Real-Time Sensor Monitoring System

print("=== Real-Time Monitoring System ===")
print("")

# Configuration
let threshold_high = 100
let threshold_low = 10
let window_size = 10

# Initialize stream
let stream = create_stream("temperature_sensors", {
    "buffer_size": 1000,
    "window_size": window_size
})

print("Monitoring started... (Ctrl+C to stop)")
print("")

# Simulated stream processing
let readings = [25, 28, 30, 95, 32, 28, 26, 5, 29, 27]  # Simulated data

for i in range(0, len(readings)):
    let reading = readings[i]
    let timestamp = time()
    
    print("Time " + to_string(i) + ": Reading = " + to_string(reading) + "°C")
    
    # Check for anomalies
    if (reading > threshold_high) {
        print("  ⚠️  ALERT: High temperature detected!")
        send_alert("HIGH", reading, timestamp)
    } else if (reading < threshold_low) {
        print("  ⚠️  ALERT: Low temperature detected!")
        send_alert("LOW", reading, timestamp)
    } else {
        print("  ✓  Normal reading")
    }
    
    # Calculate rolling average (last 3 readings)
    if (i >= 2) {
        let recent = readings[i-2:i+1]
        let avg = mean(recent)
        print("  📊 Rolling average: " + to_string(avg) + "°C")
    }
    
    print("")
}

print("Monitoring session complete")
```
</details>

---

## 🛡️ **Part 4: Fault Tolerance**

### **Automatic Recovery**

```l1
# Configure fault tolerance
let ft_config = {
    "replication_factor": 3,
    "max_retries": 5,
    "checkpoint_interval": "300s"
}

let cluster = distributed_init(ft_config)

# Submit task with automatic retry on failure
let task = cluster_submit_task("critical-job", {
    "max_retries": 5,
    "timeout": 600,
    "fallback_node": "backup-1"
})

# Task will automatically retry if it fails
let result = cluster_wait(task)
print("Task completed with fault tolerance")
```

---

## 🎯 **Part 5: Complete Example - Distributed ML Training**

```l1
# Distributed Machine Learning Training

print("=== Distributed ML Training System ===")
print("")

# Initialize cluster
let cluster = distributed_init()
cluster_add_node("gpu-1:192.168.1.20:8:16384:GPU")
cluster_add_node("gpu-2:192.168.1.21:8:16384:GPU")
cluster_add_node("gpu-3:192.168.1.22:8:16384:GPU")
print("3-node GPU cluster initialized")
print("")

# Load training data
let train_data = read_parquet("train_data.parquet")
print("Training data loaded: " + to_string(len(train_data)) + " samples")
print("")

# Split data across nodes
let partitions = split_data(train_data, 3)

# Submit training tasks
print("Submitting distributed training tasks...")
let training_tasks = []
for i in range(0, 3):
    let task = cluster_submit_task(
        "train-partition-" + to_string(i) + ":model:train:[]:gpu-" + to_string(i+1) + ":5:1800"
    )
    training_tasks.append(task)
end
print("✓ 3 training tasks submitted")
print("")

# Monitor training
print("Training in progress...")
for i in range(0, 10):  # Simulated epochs
    let progress = cluster_get_progress(training_tasks)
    print("Epoch " + to_string(i + 1) + ": " + to_string(progress) + "% complete")
    sleep(1)
end
print("")

# Wait for completion
let trained_models = cluster_wait_all(training_tasks)
print("✓ All training tasks completed")
print("")

# Aggregate models (ensemble)
print("Aggregating models...")
let ensemble_model = aggregate_models(trained_models)
print("✓ Ensemble model created")
print("")

# Evaluate
let test_data = read_parquet("test_data.parquet")
let accuracy = evaluate_model(ensemble_model, test_data)
print("Model Accuracy: " + to_string(accuracy * 100) + "%")
print("")

print("Distributed training complete! 🚀")
print("Training time: ~" + to_string(1800 / 3) + "s (3x speedup)")
```

---

## ✅ **Knowledge Check**

1. **What is a distributed cluster?**
   <details><summary>Answer</summary>Multiple computers working together as one system</details>

2. **What is load balancing?**
   <details><summary>Answer</summary>Distributing work evenly across nodes</details>

3. **Why is fault tolerance important?**
   <details><summary>Answer</summary>Ensures system continues working even when nodes fail</details>

4. **What is stream processing?**
   <details><summary>Answer</summary>Processing data in real-time as it arrives</details>

---

## 🎓 **What You've Learned**

- ✅ Cluster initialization and management
- ✅ Parallel task distribution
- ✅ Load balancing strategies
- ✅ Fault tolerance mechanisms
- ✅ Real-time stream processing
- ✅ Distributed ML training

---

## 🚀 **Next Steps**

**Practice Projects:**
1. Build distributed web crawler
2. Create real-time analytics dashboard
3. Implement distributed ML training pipeline

👉 **[Tutorial 12: Data Visualization and Dashboards](./12_Visualization.md)**

**Progress**: [x] Tutorials 01-11 ✅

---

*© 2025 LangOne Project.*

