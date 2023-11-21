db = new Mongo().getDB('local');

db.createCollection('user');