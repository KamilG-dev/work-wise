import { API_ENDPOINT } from "./constants";

export interface Image {
    id: number;
    user_id: number;
    url: string;
}

export function imagePath(path: string) {
    return API_ENDPOINT + path;
}