export interface Alert {
  id: string;
  type: 'motion' | 'unauthorized' | 'suspicious' | 'intrusion';
  timestamp: Date;
  image: string;
  message: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
}

export interface AuthorizedFace {
  id: string;
  name: string;
  image: string;
  descriptor?: Float32Array;
}

export interface GalleryItem {
  id: string;
  image: string;
  timestamp: Date;
  type: 'unauthorized' | 'suspicious';
  label?: string;
}

export interface Settings {
  mobileNumbers: string[];
  alertEnabled: boolean;
  motionSensitivity: number;
  detectionInterval: number;
}

export interface User {
  id: string;
  username: string;
  name: string;
  role: 'admin' | 'operator' | 'viewer';
  avatar?: string;
}
