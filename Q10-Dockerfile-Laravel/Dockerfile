FROM php:8.1-alpine AS build

# Install dependencies and packages
RUN apk add --no-cache \
    bash \
    git \
    libpng-dev \
    libjpeg-turbo-dev \
    libfreetype6-dev \
    libzip-dev \
    unzip \
    && apk add --no-cache --virtual .build-deps \
    build-base \
    autoconf \
    bzip2-dev \
    curl-dev \
    gcc \
    g++ \
    make \
    libxml2-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install pdo_mysql mbstring zip gd \
    && apk del .build-deps

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www

COPY . .

# Install PHP dependencies using Composer
RUN composer install --no-dev --optimize-autoloader

# Stage 2: Running application
FROM php:8.1-fpm-alpine AS production

WORKDIR /var/www

# Install only runtime dependencies (no build tools)
RUN apk add --no-cache \
    libpng-dev \
    libjpeg-turbo-dev \
    libfreetype6-dev \
    libzip-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install pdo_mysql mbstring zip gd

RUN chown -R www-data:www-data /var/www \
    && chmod -R 755 /var/www

COPY --from=build /var/www /var/www

EXPOSE 9000
CMD ["php-fpm"]