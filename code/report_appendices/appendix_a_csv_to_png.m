% Extracted from Appendix A of the original 2024 project report.
% Historical listing: see code/README.md before use.

% Veri klasörü yolu
klasor_yolu = "C:\Users\oztur\Desktop\200_TEST - Kopya\HASTALIKLI";

% Kaydetme klasörü
kaydetme_klasoru = "C:\Users\oztur\Desktop\200_TEST - Kopya\200_TEST_VERİ_GRAFİK_512\HASTALIKLI";  % Yeni hedef klasör

% Kaydetme klasörü mevcut değilse oluştur
if ~exist(kaydetme_klasoru, 'dir')
    mkdir(kaydetme_klasoru);
end

% Tüm CSV dosyalarını oku
dosya_listesi = dir(fullfile(klasor_yolu, '*.csv'));

for i = 1:numel(dosya_listesi)
    % CSV dosyasını oku
    dosya_adi = fullfile(klasor_yolu, dosya_listesi(i).name);
    veri = csvread(dosya_adi, 1, 0);  % İlk satır başlık olduğu için 1. satırdan başla
    
    % Veriyi böl
    wavelength = veri(:, 1);  % Dalga boyu sütunu
    absorbance = veri(:, 2);  % Absorpsiyon sütunu

    % Grafik oluştur
    figure('Visible', 'off', 'Position', [0, 0, 512, 512]);  % Figür boyutunu 720x720 olarak ayarla
    plot(wavelength, absorbance, '-b', 'LineWidth', 1);  % Grafik çiz
    
    % Grafik üzerindeki tüm metinleri kaldır
    set(gca, 'XTick', [], 'YTick', []);  % Eksende işaretçileri kaldır
    set(gca, 'XColor', 'none', 'YColor', 'none');  % Ekseni gizle
    axis off;  % Ekseni kapat
    
    % PNG dosya adını oluştur
    [~, dosya_adi_uzantisiz, ~] = fileparts(dosya_listesi(i).name);  % Dosya adını al (uzantısız)
    kaydetme_yolu = fullfile(kaydetme_klasoru, [dosya_adi_uzantisiz '.png']); % Kaydetme yolu
    
    % Grafiği 720x720 boyutunda kaydetmek için ayarları yap
    set(gcf, 'PaperUnits', 'inches');  % Kağıt birimini inç olarak ayarla
    set(gcf, 'PaperPosition', [0, 0, 512/100, 512/100]);  % Kağıt pozisyonunu ayarla
    
    % Yüksek çözünürlükte (200 DPI) PNG olarak kaydet
    print(kaydetme_yolu, '-dpng', '-r100');  % PNG formatında kayd

    % Figürü kapat
    close(gcf);  % Kaydetme işlemi tamamlandıktan sonra kapat
end
