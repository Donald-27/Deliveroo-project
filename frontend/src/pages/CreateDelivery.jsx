import React, { useEffect, useState } from "react";
import { useForm, Controller } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import axios from "../services/api";
import Input from "../components/common/Input";
import Button from "../components/common/Button";
import { v4 as uuidv4 } from "uuid";
import { Switch } from "@headlessui/react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const CreateDelivery = () => {
  const { register, handleSubmit, control, setValue } = useForm();
  const navigate = useNavigate();
  const [eco, setEco] = useState(false);
  const [templates, setTemplates] = useState([]);

  useEffect(() => {
    async function loadTemplates() {
      const { data } = await axios.get("/templates");
      setTemplates(data);
    }
    loadTemplates();
  }, []);

  const onSubmit = async (form) => {
    try {
      const payload = { ...form, eco_mode: eco };
      await axios.post("/parcels", payload);
      navigate("/dashboard");
    } catch (err) {
      console.error(err);
    }
  };

  const applyTemplate = (tmpl) => {
    Object.entries(tmpl.data).forEach(([key, val]) => setValue(key, val));
    setEco(tmpl.data.eco_mode || false);
  };

  return (
    <div className="max-w-3xl mx-auto p-6 bg-white shadow rounded">
      <h2 className="text-2xl font-bold text-primary mb-4">Create New Delivery</h2>

      <div className="mb-4">
        <label className="block mb-1 font-medium">Use Template:</label>
        <select onChange={(e) => applyTemplate(templates[e.target.value])} className="border p-2 rounded w-full">
          <option value="">-- Select Template --</option>
          {templates.map((t, i) => (
            <option key={t.id} value={i}>{t.name}</option>
          ))}
        </select>
      </div>

      <form onSubmit={handleSubmit(onSubmit)}>
        <Input label="Sender Address" {...register("origin")} required />
        <Input label="Recipient Address" {...register("destination")} required />
        <Input label="Weight (kg)" type="number" step="0.1" {...register("weight_kg")} required />

        <div className="mb-4 flex items-center">
          <span className="mr-4 font-medium">Eco Mode</span>
          <Switch
            checked={eco}
            onChange={setEco}
            className={`${eco ? "bg-green-500" : "bg-gray-200"} relative inline-flex items-center h-6 rounded-full w-11 transition-colors`}
          >
            <span
              className={`${eco ? "translate-x-6" : "translate-x-1"} inline-block w-4 h-4 transform bg-white rounded-full transition-transform`}
            />
          </Switch>
        </div>

        <div className="mb-4">
          <label className="block mb-1 font-medium">Schedule Delivery</label>
          <Controller
            control={control}
            name="scheduled_at"
            render={({ field }) => (
              <DatePicker
                placeholderText="Select date & time"
                showTimeSelect
                dateFormat="Pp"
                className="border p-2 rounded w-full"
                selected={field.value}
                onChange={(d) => field.onChange(d)}
              />
            )}
          />
        </div>

        <div className="mb-4">
          <label className="block mb-1 font-medium">Special Instructions</label>
          <textarea {...register("instructions")} className="w-full border p-2 rounded" rows={3} />
        </div>

        <Button type="submit">Submit Delivery</Button>
      </form>
    </div>
  );
};

export default CreateDelivery;
