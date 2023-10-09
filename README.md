# Vital-Sound-Imitator-AI
AI that will hear a synthesizer sound and recreate it with vital synth

How do I get a trainable amount of sound matched with its parameters??
Do I automate? 
  -Research into how synth generate sound.   
  -look at how parameters are passed into the synth as what datatypes
  -look to automate the process and save input and output as a pair of files 
Look at .vital files

Probably easier than expected, will just have to process .vital files (in json)
  -use free give presets first
 -do need way more

 UPDATE: vital file has wave form data encoded into it.
 json WaveSourceKeyframe::stateToJson() {
  String encoded = Base64::toBase64(wave_frame_->time_domain, sizeof(float) * vital::WaveFrame::kWaveformSize);
  json data = WavetableKeyframe::stateToJson();
  data["wave_data"] = encoded.toStdString();
  return data;
}

void WaveSourceKeyframe::jsonToState(json data) {
  WavetableKeyframe::jsonToState(data);

  MemoryOutputStream decoded(sizeof(float) * vital::WaveFrame::kWaveformSize);
  std::string wave_data = data["wave_data"];
  Base64::convertFromBase64(decoded, wave_data);
  memcpy(wave_frame_->time_domain, decoded.getData(), sizeof(float) * vital::WaveFrame::kWaveformSize);
  wave_frame_->toFrequencyDomain();
}

FEATURES: 
Properties of a sound  (further research)

LABELS:   list of these values?
OSC 1 
0. Mix  (0,1)
1. Wave Shape  (output as what? polynomial function??)
2. Unison Amount  (1,16)
3. Unison %      (0,100)
4. Phase angle   (0,360)
5. Phase %       (0,100)
6. Filter/Effect  
OSC2  same
OSC3  ame 
SMP 
0. Mix  (0,1)
1. Noise Type
2. Sample Transpose  (-48,48)
3. Sample Tune (-100, 100)
4. Level       (0,1) 
5. Pan%         (-100,100)
6. Filter/Effect 

Wait I should just get the data from vital itself... stop calculating. 