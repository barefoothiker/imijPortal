import { Sample } from './../models/sample';

export class Patient {
    id: number;
    daphniId: number;
    userStoryId:number;
    samples:Sample[];
}
