# Specify the log directory or experiment ID
log_dir =  r"C:\Users\cyberwitch\Documents\code_projects\ALTR_CORE\logs\tf_logs\training_log_2024_12_27__18_26_22"
import traceback
import pandas as pd
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator

# Extraction function
def tflog2pandas(path):
    runlog_data = pd.DataFrame({"metric": [], "value": [], "step": []})
    try:
        # Pass size_guidance argument to lift the limit for scalars
        event_acc = EventAccumulator(path, size_guidance={"scalars": 0})
        event_acc.Reload()

        # Check available tags in the logs
        tags = event_acc.Tags()
        print(tags)  # This will show available tags in the log files

        # Proceed with extracting scalar data if available
        if "scalars" in tags:
            scalar_tags = tags["scalars"]
            for tag in scalar_tags:
                event_list = event_acc.Scalars(tag)
                values = list(map(lambda x: x.value, event_list))
                step = list(map(lambda x: x.step, event_list))
                r = {"metric": [tag] * len(step), "value": values, "step": step}
                r = pd.DataFrame(r)
                runlog_data = pd.concat([runlog_data, r])

        tags = event_acc.Tags()
        
        print("Tags:", tags)

        # Check available tensor data
        if "tensors" in tags:
            tensor_tags = tags["tensors"]
            for tag in tensor_tags:
                tensor_data = event_acc.Tensors(tag)
                print(f"Tensor data for {tag}: {tensor_data}")

        else:
            print("No scalar data found.")

    except Exception:
        print("Event file possibly corrupt: {}".format(path))
        traceback.print_exc()
    
    return runlog_data

path = log_dir  # folderpath
df = tflog2pandas(path)
df.to_csv("output.csv")
