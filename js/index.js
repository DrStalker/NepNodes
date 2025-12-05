import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";
import { api } from '../../scripts/api.js';

app.registerExtension({
  name: "NepStylesCat",
  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    if (nodeData.name === "NepStylesCat") {

      const onNodeCreated = nodeType.prototype.onNodeCreated;
      nodeType.prototype.onNodeCreated = function () {
        onNodeCreated ? onNodeCreated.apply(this, []) : undefined;


        loraNameWidget.callback = () => {
          const value = loraNameWidget.value;

          const body = new FormData();
          body.append("lora_name", value);
          api
            .fetchApi("/lora_info", { method: "POST", body })
            .then((response) => response.json())
            .then((resp) => {
              baseModelWidget.value = resp.baseModel;
              outputWidget.value = resp.output;
            });
        };
      }

      const onExecuted = nodeType.prototype.onExecuted;
      nodeType.prototype.onExecuted = function (message) {
        onExecuted?.apply(this, [message]);
        this.showValueWidget.value = message.text[0];
        this.baseModelWidget.value = message.model[0];
      }
    }
  },
});
