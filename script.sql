ALTER TABLE lawyer_images ADD UNIQUE (id_lawyer);

ALTER TABLE lawyer_images MODIFY COLUMN image_url VARCHAR(500);