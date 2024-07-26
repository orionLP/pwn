class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable
  has_one_attached :avatar
  after_commit :add_default_avatar, on: %i[create update]
  validate :avatar_content_type
  validate :avatar_size
  def avatar_thumbnail
    if avatar.attached? && valid?
      avatar.variant(resize: "150x150!").processed
    else
        '/default_profile.png'
    end
  end
  
  private
  def add_default_avatar
    unless avatar.attached?
      avatar.attach(
        io: File.open(
          Rails.root.join(
            'app', 'assets', 'images', 'default_profile.png'
          )
        ), 
        filename: 'default_profile.png',
        content_type: 'image/png'
      )
    end
  end
  def avatar_content_type
    if avatar.attached? && !avatar.content_type.in?(%w(image/png))
      errors.add(:avatar, "must be a PNG image")
    end
  end
  def avatar_size
    if avatar.attached? && avatar.blob.byte_size > 5.megabytes
      errors.add(:avatar, "should be less than 5MB")
    end
  end
end
